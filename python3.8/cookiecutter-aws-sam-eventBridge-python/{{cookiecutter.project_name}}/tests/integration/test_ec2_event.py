import logging
import os
from time import sleep, time
from unittest import TestCase

import boto3


class TestEC2Event(TestCase):
    """
    This integration test will create an EC2 and verify the lambda function is invoked by checking the cloudwatch log
    The EC2 instance will be deleted when test completes.
    """

    function_name: str
    instance_id: str  # temporary EC2 instance ID

    @classmethod
    def setUpClass(cls) -> None:
        """
        Based on the provided env variable AWS_SAM_STACK_NAME,
        here we use cloudformation API to find out what the HelloWorldFunction function name
        """
        stack_name = os.environ.get("AWS_SAM_STACK_NAME")
        if not stack_name:
            raise Exception("Cannot find env var AWS_SAM_STACK_NAME")

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
        """
        Create a temporary EC2 instance, and record the instance id for verification and clean up
        """
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
        """
        Clean up the EC2 instance
        """
        client = boto3.client("ec2")
        client.terminate_instances(InstanceIds=[self.instance_id])

    def test_ec2_event(self):
        """
        Scan the cloudwatch log in the past minute to verify there is a log entry
        containing the EC2 instance ID recorded in setUp().
        Since cloudwatch log has a latency, here we will retry 5 times
        """
        log_group_name = f"/aws/lambda/{self.function_name}"

        client = boto3.client("logs")

        # cloudwatch log might be deplayed, give it 5 retries
        retries = 5
        start_time = int(time() - 60) * 1000
        while retries >= 0:
            response = client.describe_log_streams(
                logGroupName=log_group_name,
                orderBy="LastEventTime",
                descending=True,
            )
            log_streams = response["logStreams"]
            self.assertTrue(log_streams, "Cannot find log streams")

            # use the lastest one
            log_stream = log_streams[0]

            response = client.get_log_events(
                logGroupName=log_group_name,
                logStreamName=log_stream["logStreamName"],
                startTime=start_time,
                endTime=int(time()) * 1000,
                startFromHead=False,
            )
            events = response["events"]
            match_events = [event for event in events if self.instance_id in event["message"]]
            if match_events:
                return
            else:
                logging.info(f"Cannot find matching events containing instance id {self.instance_id}, waiting")
                retries -= 1
                sleep(5)

        self.fail(f"Cannot find matching events containing instance id {self.instance_id} after 5 retries")
