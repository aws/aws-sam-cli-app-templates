# import requests

from model.aws.ec2 import Marshaller
from model.aws.ec2 import AWSEvent
from model.aws.ec2 import EC2InstanceStateChangeNotification


def lambda_handler(event, context):
    """Sample Lambda function reacting to EventBridge events

    Parameters
    ----------
    event: dict, required
        Event Bridge EC2 State Change Events Format

        Event doc: https://docs.aws.amazon.com/eventbridge/latest/userguide/event-types.html#ec2-event-type

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
        The same input event file
    """

    #Deserialize event into strongly typed object
    awsEvent:AWSEvent = Marshaller.unmarshall(event, AWSEvent)
    ec2StateChangeNotification:EC2InstanceStateChangeNotification = awsEvent.detail

    #Execute business logic
    print("Instance " + ec2StateChangeNotification.instance_id + " transitioned to " + ec2StateChangeNotification.state)

    #Make updates to event payload
    awsEvent.detail_type = "HelloWorldFunction updated event of " + awsEvent.detail_type;

    #Return event for further processing
    return Marshaller.marshall(awsEvent)
