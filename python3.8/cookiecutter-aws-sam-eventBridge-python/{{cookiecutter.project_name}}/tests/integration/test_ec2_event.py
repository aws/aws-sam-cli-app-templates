import logging
import os
from time import sleep, time
from unittest import TestCase

import boto3
from botocore.exceptions import ClientError

"""
Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test. 
"""


class TestEC2Event(TestCase):
    """
    This integration test will create an EC2 and verify the lambda function is invoked by checking the cloudwatch log
    The EC2 instance will be deleted when test completes.
    """

    function_name: str
    instance_id: str  # temporary EC2 instance ID

    @classmethod
    def get_and_verify_stack_name(cls) -> str:
        stack_name = os.environ.get("AWS_SAM_STACK_NAME")
        if not stack_name:
            raise Exception(
                "Cannot find env var AWS_SAM_STACK_NAME. \n"
                "Please setup this environment variable with the stack name where we are running integration tests."
            )

        # Verify stack exists
        client = boto3.client("cloudformation")
        try:
            client.describe_stacks(StackName=stack_name)
        except Exception as e:
            raise Exception(
                f"Cannot find stack {stack_name}. \n" f'Please make sure stack with the name "{stack_name}" exists.'
            ) from e

        return stack_name

    @classmethod
    def setUpClass(cls) -> None:
        stack_name = TestEC2Event.get_and_verify_stack_name()

        client = boto3.client("cloudformation")
        response = client.list_stack_resources(StackName=stack_name)
        resources = response["StackResourceSummaries"]
        function_resources = [
            resource for resource in resources if resource["LogicalResourceId"] == "HelloWorldFunction"
        ]
        if not function_resources:
            raise Exception("Cannot find HelloWorldFunction")

        cls.function_name = function_resources[0]["PhysicalResourceId"]

    def setUp(self) -> None:
        client = boto3.client("ec2")
        response = client.run_instances(
            ImageId="resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2",
            InstanceType="t2.nano",
            MaxCount=1,
            MinCount=1,
        )
        self.assertIn("Instances", response, "Fail to create an EC2 instance")
        self.instance_id = response["Instances"][0]["InstanceId"]

    def tearDown(self) -> None:
        client = boto3.client("ec2")
        client.terminate_instances(InstanceIds=[self.instance_id])

    def test_ec2_event(self):
        log_group_name = f"/aws/lambda/{self.function_name}"

        # cloudwatch log might be deplayed, give it 5 retries
        retries = 5
        start_time = int(time() - 60) * 1000
        while retries >= 0:
            # use the lastest one
            log_stream_name = self._get_latest_log_stream_name(log_group_name)
            if not log_stream_name:
                sleep(5)
                continue

            match_events = self._get_matched_events(log_group_name, log_stream_name, start_time)
            if match_events:
                return
            else:
                logging.info(f"Cannot find matching events containing instance id {self.instance_id}, waiting")
                retries -= 1
                sleep(5)

        self.fail(f"Cannot find matching events containing instance id {self.instance_id} after 5 retries")

    def _get_latest_log_stream_name(self, log_group_name: str):
        """
        Find the name of latest log stream name in group,
        return None if the log group does not exists or does not have any stream
        (for lambda function that has never invoked before).
        """
        client = boto3.client("logs")
        try:
            response = client.describe_log_streams(
                logGroupName=log_group_name,
                orderBy="LastEventTime",
                descending=True,
            )
        except ClientError as e:
            if e.response["Error"]["Code"] == "ResourceNotFoundException":
                logging.info(f"Cannot find log group {log_group_name}, waiting")
                return None
            raise e

        log_streams = response["logStreams"]
        self.assertTrue(log_streams, "Cannot find log streams")

        # use the lastest one
        return log_streams[0]

    def _get_matched_events(self, log_group_name, log_stream_name, start_time):
        """
        Return a list of events with body containing self.instance_id after start_time
        """
        client = boto3.client("logs")
        response = client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            startTime=start_time,
            endTime=int(time()) * 1000,
            startFromHead=False,
        )
        events = response["events"]
        return [event for event in events if self.instance_id in event["message"]]
