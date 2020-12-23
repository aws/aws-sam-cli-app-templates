"use strict";

const chai = require("chai");
const AWS = require("aws-sdk");
const uuid = require("uuid");
const expect = chai.expect;

const sleep = (secs) =>
  new Promise((resolve) => setTimeout(resolve, 1000 * secs));

/**
 * This integration test will execute the step function and verify
 * - "Record Transaction" is executed
 * - the record has been inserted into the transaction record
 *
 * Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test.
 */
describe("Test State Machine", function () {
  let stateMachineArn, transactionTableName;

  let executionArn, transactionTableInput;

  /**
   * Based on the provided env variable AWS_SAM_STACK_NAME,
   * here we use cloudformation API to find out:
   * - StockTradingStateMachine's ARN
   * - TransactionTable's table name
   */
  before(async () => {
    const stackName = process.env["AWS_SAM_STACK_NAME"];
    if (!stackName) {
      throw new Error("Cannot find env var AWS_SAM_STACK_NAME");
    }

    const client = new AWS.CloudFormation();
    const response = await client
      .listStackResources({
        StackName: stackName,
      })
      .promise();

    const resources = response.StackResourceSummaries;

    const stateMachineResource = resources.find(
      (resource) => resource.LogicalResourceId === "StockTradingStateMachine"
    );
    expect(
      stateMachineResource,
      `Cannot find StockTradingStateMachine in stack ${stackName}`
    ).not.to.be.undefined;

    const transactionTableResource = resources.find(
      (resource) => resource.LogicalResourceId === "TransactionTable"
    );
    expect(
      transactionTableResource,
      `Cannot find TransactionTable in stack ${stackName}`
    ).not.to.be.undefined;

    stateMachineArn = stateMachineResource.PhysicalResourceId;
    transactionTableName = transactionTableResource.PhysicalResourceId;
  });

  /**
   * Delete the dynamodb table item that are created during the test
   */
  afterEach(() => {
    const client = new AWS.DynamoDB();
    return client
      .deleteItem({
        Key: {
          Id: {
            S: transactionTableInput["id"],
          },
        },
        TableName: transactionTableName,
      })
      .promise();
  });

  /**
   * Start the state machine execution request and record the execution ARN
   */
  const startExecution = async () => {
    const client = new AWS.StepFunctions();
    const response = await client
      .startExecution({
        stateMachineArn,
        name: `integ-test-${uuid.v4()}`,
        input: "{}",
      })
      .promise();

    executionArn = response.executionArn;
  };

  const waitExecution = async () => {
    const client = new AWS.StepFunctions();
    while (true) {
      const response = await client
        .describeExecution({ executionArn })
        .promise();

      switch (response.status) {
        case "SUCCEEDED":
          console.log(`Execution ${executionArn} completed`);
          return;
        case "RUNNING":
          console.log(`Execution ${executionArn} is still running, waiting`);
          await sleep(3);
          break;
        default:
          throw new Error(
            `Execution ${executionArn} failed with status ${response.status}`
          );
      }
    }
  };

  /**
   * Make sure "Record Transaction" step was reached, and record the input of it.
   */
  const retrieveTransactionTableInput = async () => {
    const client = new AWS.StepFunctions();
    const response = await client
      .getExecutionHistory({ executionArn })
      .promise();

    const events = response.events;
    const recordTransactionEnteredEvent = events.find(
      (event) =>
        event.type === "TaskStateEntered" &&
        event.stateEnteredEventDetails.name === "Record Transaction"
    );
    expect(
      recordTransactionEnteredEvent,
      "Cannot find Record Transaction TaskStateEntered event"
    ).to.not.be.undefined;

    transactionTableInput = JSON.parse(
      recordTransactionEnteredEvent.stateEnteredEventDetails.input
    );
  };

  /**
   * Use the input recorded in _retrieve_transaction_table_input() to
   * verify whether the record has been written to dynamodb
   */
  const verifyTransactionRecordWritten = async () => {
    const client = new AWS.DynamoDB();
    const response = await client
      .getItem({
        Key: {
          Id: {
            S: transactionTableInput["id"],
          },
        },
        TableName: transactionTableName,
      })
      .promise();

    expect(response.Item).not.to.be.undefined;
    expect(response.Item).to.deep.include({
      Quantity: { N: transactionTableInput["qty"] },
      Price: { N: transactionTableInput["price"] },
      Type: { S: transactionTableInput["type"] },
    });
  };

  it("Test state machine execution", async () => {
    await startExecution();
    await waitExecution();
    await retrieveTransactionTableInput();
    await verifyTransactionRecordWritten();
  });
});
