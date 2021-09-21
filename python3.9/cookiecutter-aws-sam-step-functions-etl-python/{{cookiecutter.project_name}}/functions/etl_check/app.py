import boto3
import json
from datetime import datetime

session = boto3.session.Session()
client = session.client("glue")

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        Glue StartJobRun response object

        {
            "JobName": "your_job_name",
            "JobRunId": "jr_uuid",
            "SdkHttpMetadata": {
                "AllHttpHeaders": {
                    "Connection": ["keep-alive"],
                    "x-amzn-RequestId": ["12345678-abcd-abcd-1234-0123456789ab"],
                    "Content-Length": ["1234"],
                    "Date": ["Mon, 20 Sep 2021 19:41:48 GMT"],
                    "Content-Type": ["application/x-amz-json-1.1"]
                },
                "HttpHeaders": {
                    "Connection": "keep-alive",
                    "Content-Length": "1234",
                    "Content-Type": "application/x-amz-json-1.1",
                    "Date": "Mon, 20 Sep 2021 19:41:48 GMT",
                    "x-amzn-RequestId": "12345678-abcd-abcd-1234-0123456789ab"
                },
                "HttpStatusCode": 200
            },
            "SdkResponseMetadata": {
                "RequestId": "12345678-abcd-abcd-1234-0123456789ab"
            }
        }

    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    Output for the next state in the Step Function workflow
    """
    response = client.get_job_run(
        JobName=event["JobName"],
        RunId=event["JobRunId"]
    )
    print(json.dumps(response, cls=DateTimeEncoder))
    output = {
        "JobName": event["JobName"],
        "JobRunId": event["JobRunId"],
        "JobRunState": response["JobRun"]["JobRunState"],
        "StartedOn": response["JobRun"]["StartedOn"].isoformat()
    }
    if response["JobRun"]["JobRunState"] in ["SUCCEEDED", "FAILED"]:
        output["CompletedOn"] = response["JobRun"]["CompletedOn"].isoformat()
        output["ExecutionTime"] = response["JobRun"]["ExecutionTime"]
    return output
