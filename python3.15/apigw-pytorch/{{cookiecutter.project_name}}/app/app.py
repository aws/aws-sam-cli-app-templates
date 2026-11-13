import torch
import torchvision
import base64
import json
import numpy as np

import torch.nn as nn
import torch.nn.functional as F

from PIL import Image
from io import BytesIO

image_transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.1307,), (0.3081,))])


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, kernel_size=5)
        self.conv2 = nn.Conv2d(20, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()

        self.fc1 = nn.Linear(320, 100)
        self.bn1 = nn.BatchNorm1d(100)

        self.fc2 = nn.Linear(100, 100)
        self.bn2 = nn.BatchNorm1d(100)

        self.smax = nn.Linear(100, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))

        x = x.view(-1, 320)
        x = self.bn1(F.relu(self.fc1(x)))
        x = F.dropout(x, training=self.training)

        x = self.bn2(F.relu(self.fc2(x)))
        x = F.dropout(x, training=self.training)

        return F.softmax(self.smax(x), dim=-1)


model_file = '/opt/ml/model'
model = Net()
model.load_state_dict(torch.load(model_file))
model.eval()


def lambda_handler(event, context):
    image_bytes = event['body'].encode('utf-8')
    image = Image.open(BytesIO(base64.b64decode(image_bytes))).convert(mode='L')
    image = image.resize((28, 28))

    probabilities = model.forward(image_transforms(np.array(image)).reshape(-1, 1, 28, 28))
    label = torch.argmax(probabilities).item()

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "predicted_label": label,
            }
        )
    }
