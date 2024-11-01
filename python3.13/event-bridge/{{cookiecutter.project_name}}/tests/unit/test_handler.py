import pytest

from hello_world import app
from model.aws.ec2 import AWSEvent
from model.aws.ec2.ec2_instance_state_change_notification import EC2InstanceStateChangeNotification
from model.aws.ec2 import Marshaller

@pytest.fixture()
def eventBridgeec2InstanceEvent():
    """ Generates EventBridge EC2 Instance Notification Event"""

    return {
            "version":"0",
            "id":"7bf73129-1428-4cd3-a780-95db273d1602",
            "detail-type":"EC2 Instance State-change Notification",
            "source":"aws.ec2",
            "account":"123456789012",
            "time":"2015-11-11T21:29:54Z",
            "region":"us-east-1",
            "resources":[
              "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"
            ],
            "detail":{
              "instance-id":"i-abcd1111",
              "state":"pending"
            }
    }


def test_lambda_handler(eventBridgeec2InstanceEvent, mocker):

    ret = app.lambda_handler(eventBridgeec2InstanceEvent, "")

    awsEventRet:AWSEvent = Marshaller.unmarshall(ret, AWSEvent)
    detailRet:EC2InstanceStateChangeNotification = awsEventRet.detail

    assert detailRet.instance_id == "i-abcd1111"
    assert awsEventRet.detail_type.startswith("HelloWorldFunction updated event of ")