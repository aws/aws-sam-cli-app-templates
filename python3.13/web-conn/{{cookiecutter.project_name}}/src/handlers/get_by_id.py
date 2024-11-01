import json
import os
import boto3

client = boto3.client('dynamodb')

def getByIdHandler(event, context):
    if event["httpMethod"] != "GET":
        raise Exception(f"getByIdHandler only accept GET method, you tried: {event.httpMethod}")

    id = event["pathParameters"]["id"]
    data = client.get_item(TableName=os.environ["SAMPLE_TABLE"], Key={"id": {"S": id}})
    item = data["Item"]
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
