import base64
import json
import numpy as np
import tensorflow as tf

from PIL import Image
from io import BytesIO


model_file = '/opt/ml/model'
model = tf.keras.models.load_model(model_file)


def lambda_handler(event, context):
    image_bytes = event['body'].encode('utf-8')
    image = Image.open(BytesIO(base64.b64decode(image_bytes))).convert(mode='L')
    image = image.resize((28, 28))

    probabilities = model(np.array(image).reshape(-1, 28, 28, 1))
    label = np.argmax(probabilities)

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "predicted_label": int(label),
            }
        )
    }
