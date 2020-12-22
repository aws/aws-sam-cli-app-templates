import os
from unittest import TestCase

import boto3
import requests


class TestApiGateway(TestCase):
    api_endpoint: str

    def setUp(self) -> None:
        """
        Based on the provided env variable AWS_SAM_STACK_NAME,
        here we use cloudformation API to find out what the HelloWorldApi URL is
        """
        stack_name = os.environ.get("AWS_SAM_STACK_NAME")
        self.failIf(not stack_name, "Cannot find env var AWS_SAM_STACK_NAME")

        client = boto3.client("cloudformation")

        response = client.describe_stacks(StackName=stack_name)
        stacks = response["Stacks"]
        self.assertTrue(stacks, f"Cannot find stack {stack_name}")

        stack_outputs = stacks[0]["Outputs"]
        api_outputs = [output for output in stack_outputs if output["OutputKey"] == "HelloWorldApi"]
        self.assertTrue(api_outputs, f"Cannot find output HelloWorldApi in stack {stack_name}")

        self.api_endpoint = api_outputs[0]["OutputValue"]

    def test_api_gateway(self):
        """
        Call the API Gateway endpoint and check the response
        """
        response = requests.get(self.api_endpoint)
        self.assertDictEqual(response.json(), {"message": "hello world"})
