import base64
import json
import numpy as np

from io import BytesIO
from PIL import Image

import xgboost as xgb

model_file = '/opt/ml/model'
model = xgb.Booster()
model.load_model(model_file)


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
