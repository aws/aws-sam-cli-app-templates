import os
from unittest import TestCase

import boto3
import requests


class TestApiGateway(TestCase):
    api_endpoint: str

    def setUp(self) -> None:
        stack_name = os.environ.get("AWS_SAM_STACK_NAME")
        self.failIf(not stack_name, 'Cannot find env var AWS_SAM_STACK_NAME')

        client = boto3.client("cloudformation")
        response = client.list_stack_resources(StackName=stack_name)
        resources = response["StackResourceSummaries"]
        api_resources = [
            resource
            for resource in resources
            if resource["LogicalResourceId"] == "ServerlessRestApi"
        ]
        self.failIf(not api_resources, "Cannot find ServerlessRestApi")

        self.api_endpoint = f"https://{api_resources[0]['PhysicalResourceId']}.execute-api.{client.meta.region_name}.amazonaws.com/Prod/hello/"

    def test_api_gateway(self):
        response = requests.get(self.api_endpoint)
        self.assertIn('file_contents', response.json())
        self.assertIn('created_file', response.json())
