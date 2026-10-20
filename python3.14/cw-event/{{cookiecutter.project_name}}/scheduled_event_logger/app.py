import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """Sample Lambda function that logs the payload of a scheduled event

    Parameters
    ----------
    event: dict, required
        EventBridge Scheduled Event Input Format

        Event doc: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    """

    # All log statements are written to CloudWatch Logs by default. For more information, see
    # https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html
    logger.info(json.dumps(event))
