import json
import os
import boto3

client = boto3.client('dynamodb')

def putItemHandler(event, context):
    if event["httpMethod"] != "POST":
        raise Exception(f"putItemHandler only accept POST method, you tried: {event.httpMethod}")

    # Get id and name from the body of the request
    body = json.loads(event["body"])
    id = body["id"]
    name = body["name"]

    result = client.put_item(TableName=os.environ["SAMPLE_TABLE"], Item={"id": {"S": id}, "name": {"S": name}})
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
