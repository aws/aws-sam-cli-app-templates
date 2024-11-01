import json
import logging
import os
from time import sleep
from typing import Dict
from unittest import TestCase
from uuid import uuid4

import boto3
from botocore.client import BaseClient

"""
Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test. 
"""


class TestStateMachine(TestCase):
    """
    This integration test will execute the step function and verify
    - "Record Transaction" is executed
    - the record has been inserted into the transaction record table.
    * The inserted record will be removed when test completed.
    """

    state_machine_arn: str
    transaction_table_name: str

    client: BaseClient
    inserted_record_id: str

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
        """
        Based on the provided env variable AWS_SAM_STACK_NAME,
        here we use cloudformation API to find out:
        - StockTradingStateMachine's ARN
        - TransactionTable's table name
        """
        stack_name = TestStateMachine.get_and_verify_stack_name()

        client = boto3.client("cloudformation")
        response = client.list_stack_resources(StackName=stack_name)
        resources = response["StackResourceSummaries"]
        state_machine_resources = [
            resource for resource in resources if resource["LogicalResourceId"] == "StockTradingStateMachine"
        ]
        transaction_table_resources = [
            resource for resource in resources if resource["LogicalResourceId"] == "TransactionTable"
        ]
        if not state_machine_resources or not transaction_table_resources:
            raise Exception("Cannot find StockTradingStateMachine or TransactionTable")

        cls.state_machine_arn = state_machine_resources[0]["PhysicalResourceId"]
        cls.transaction_table_name = transaction_table_resources[0]["PhysicalResourceId"]

    def setUp(self) -> None:
        self.client = boto3.client("stepfunctions")

    def tearDown(self) -> None:
        """
        Delete the dynamodb table item that are created during the test
        """
        client = boto3.client("dynamodb")
        client.delete_item(
            Key={
                "Id": {
                    "S": self.inserted_record_id,
                },
            },
            TableName=self.transaction_table_name,
        )

    def _start_execute(self) -> str:
        """
        Start the state machine execution request and record the execution ARN
        """
        response = self.client.start_execution(
            stateMachineArn=self.state_machine_arn, name=f"integ-test-{uuid4()}", input="{}"
        )
        return response["executionArn"]

    def _wait_execution(self, execution_arn: str):
        while True:
            response = self.client.describe_execution(executionArn=execution_arn)
            status = response["status"]
            if status == "SUCCEEDED":
                logging.info(f"Execution {execution_arn} completely successfully.")
                break
            elif status == "RUNNING":
                logging.info(f"Execution {execution_arn} is still running, waiting")
                sleep(3)
            else:
                self.fail(f"Execution {execution_arn} failed with status {status}")

    def _retrieve_transaction_table_input(self, execution_arn: str) -> Dict:
        """
        Make sure "Record Transaction" step was reached, and record the input of it.
        """
        response = self.client.get_execution_history(executionArn=execution_arn)
        events = response["events"]
        record_transaction_entered_events = [
            event
            for event in events
            if event["type"] == "TaskStateEntered" and event["stateEnteredEventDetails"]["name"] == "Record Transaction"
        ]
        self.assertTrue(
            record_transaction_entered_events,
            "Cannot find Record Transaction TaskStateEntered event",
        )
        transaction_table_input = json.loads(record_transaction_entered_events[0]["stateEnteredEventDetails"]["input"])
        self.inserted_record_id = transaction_table_input["id"]  # save this ID for cleaning up
        return transaction_table_input

    def _verify_transaction_record_written(self, transaction_table_input: Dict):
        """
        Use the input recorded in _retrieve_transaction_table_input() to
        verify whether the record has been written to dynamodb
        """
        client = boto3.client("dynamodb")
        response = client.get_item(
            Key={
                "Id": {
                    "S": transaction_table_input["id"],
                },
            },
            TableName=self.transaction_table_name,
        )
        self.assertTrue(
            "Item" in response,
            f'Cannot find transaction record with id {transaction_table_input["id"]}',
        )
        item = response["Item"]
        self.assertDictEqual(item["Quantity"], {"N": transaction_table_input["qty"]})
        self.assertDictEqual(item["Price"], {"N": transaction_table_input["price"]})
        self.assertDictEqual(item["Type"], {"S": transaction_table_input["type"]})

    def test_state_machine(self):
        execution_arn = self._start_execute()
        self._wait_execution(execution_arn)
        transaction_table_input = self._retrieve_transaction_table_input(execution_arn)
        self._verify_transaction_record_written(transaction_table_input)
