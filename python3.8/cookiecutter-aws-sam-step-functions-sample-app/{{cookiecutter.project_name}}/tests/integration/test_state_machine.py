import json
import logging
import os
from time import sleep
from typing import Dict
from unittest import TestCase
from uuid import uuid4

import boto3
from botocore.client import BaseClient


class TestStateMachine(TestCase):
    """
    This integration test will execute the step function and verify the record has been inserted into
    then transaction record table.
    The inserted record will be removed when test completed.
    """

    state_machine_arn: str
    transaction_table_name: str

    client: BaseClient
    execution_name: str
    execution_arn: str
    transaction_table_input: Dict

    @classmethod
    def setUpClass(cls) -> None:
        stack_name = os.environ.get("AWS_SAM_STACK_NAME")
        if not stack_name:
            raise Exception("Cannot find env var AWS_SAM_STACK_NAME")

        client = boto3.client("cloudformation")
        response = client.list_stack_resources(StackName=stack_name)
        resources = response["StackResourceSummaries"]
        state_machine_resources = [
            resource
            for resource in resources
            if resource["LogicalResourceId"] == "StockTradingStateMachine"
        ]
        transaction_table_resources = [
            resource
            for resource in resources
            if resource["LogicalResourceId"] == "TransactionTable"
        ]
        if not state_machine_resources or not transaction_table_resources:
            raise Exception("Cannot find StockTradingStateMachine or TransactionTable")

        cls.state_machine_arn = state_machine_resources[0]["PhysicalResourceId"]
        cls.transaction_table_name = transaction_table_resources[0][
            "PhysicalResourceId"
        ]

    def setUp(self) -> None:
        self.execution_name = f"integ-test-{uuid4()}"
        self.client = boto3.client("stepfunctions")

    def tearDown(self) -> None:
        client = boto3.client("dynamodb")
        client.delete_item(
            Key={"Id": {"S": self.transaction_table_input["id"],},},
            TableName=self.transaction_table_name,
        )

    def _start_execute(self):
        response = self.client.start_execution(
            stateMachineArn=self.state_machine_arn, name=self.execution_name, input="{}"
        )
        self.execution_arn = response["executionArn"]

    def _wait_execution(self):
        while True:
            response = self.client.describe_execution(executionArn=self.execution_arn)
            status = response["status"]
            if status == "SUCCEEDED":
                logging.info(f"Execution {self.execution_arn} completely successfully.")
                break
            elif status == "RUNNING":
                logging.info(
                    f"Execution {self.execution_arn} is still running, waiting"
                )
                sleep(3)
            else:
                self.fail(f"Execution {self.execution_arn} failed with status {status}")

    def _retrieve_transaction_table_input(self):
        response = self.client.get_execution_history(executionArn=self.execution_arn)
        events = response["events"]
        record_transaction_entered_events = [
            event
            for event in events
            if event["type"] == "TaskStateEntered"
            and event["stateEnteredEventDetails"]["name"] == "Record Transaction"
        ]
        self.assertTrue(
            record_transaction_entered_events,
            "Cannot find Record Transaction TaskStateEntered event",
        )
        self.transaction_table_input = json.loads(
            record_transaction_entered_events[0]["stateEnteredEventDetails"]["input"]
        )

    def _verify_transaction_record_written(self):
        client = boto3.client("dynamodb")
        response = client.get_item(
            Key={"Id": {"S": self.transaction_table_input["id"],},},
            TableName=self.transaction_table_name,
        )
        self.assertTrue(
            "Item" in response,
            f'Cannot find transaction record with id {self.transaction_table_input["id"]}',
        )
        item = response["Item"]
        self.assertDictEqual(
            item["Quantity"], {"N": self.transaction_table_input["qty"]}
        )
        self.assertDictEqual(
            item["Price"], {"N": self.transaction_table_input["price"]}
        )
        self.assertDictEqual(item["Type"], {"S": self.transaction_table_input["type"]})

    def test_state_machine(self):
        self._start_execute()
        self._wait_execution()
        self._retrieve_transaction_table_input()
        self._verify_transaction_record_written()