import base64
import json
import numpy as np

from io import BytesIO
from PIL import Image

import xgboost as xgb
from scipy.ndimage import interpolation

model_file = '/opt/ml/model'
model = xgb.Booster()
model.load_model(model_file)


# Functions to pre-process images (we used same preprocessing when training)

def moments(image):
    c0, c1 = np.mgrid[:image.shape[0], :image.shape[1]]
    img_sum = np.sum(image)
    
    m0 = np.sum(c0 * image) / img_sum
    m1 = np.sum(c1 * image) / img_sum
    m00 = np.sum((c0-m0)**2 * image) / img_sum
    m11 = np.sum((c1-m1)**2 * image) / img_sum
    m01 = np.sum((c0-m0) * (c1-m1) * image) / img_sum
    
    mu_vector = np.array([m0,m1])
    covariance_matrix = np.array([[m00, m01],[m01, m11]])
    
    return mu_vector, covariance_matrix


def deskew(image):
    c, v = moments(image)
    alpha = v[0,1] / v[0,0]
    affine = np.array([[1,0], [alpha,1]])
    ocenter = np.array(image.shape) / 2.0
    offset = c - np.dot(affine, ocenter)

    return interpolation.affine_transform(image, affine, offset=offset)


def get_np_image(image_bytes):
    image = Image.open(BytesIO(base64.b64decode(image_bytes))).convert(mode='L')
    image = image.resize((28, 28))

    return np.array(image)


# Lambda handler code

def lambda_handler(event, context):
    image_bytes = event['body'].encode('utf-8')
    image = Image.open(BytesIO(base64.b64decode(image_bytes))).convert(mode='L')
    image = image.resize((28, 28))

    x = np.array(image).reshape(1, -1)
    prediction = int(np.argmax(model.predict(xgb.DMatrix(x))))

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "predicted_label": prediction,
            }
        )
    }
