"use strict";

const chai = require("chai");
const AWS = require("aws-sdk");
const uuid = require("uuid");
const expect = chai.expect;

const sleep = (secs) =>
  new Promise((resolve) => setTimeout(resolve, 1000 * secs));

/**
 * Get stack name from environment variable AWS_SAM_STACK_NAME and make an API call to verify the stack exists.
 * throw exception if AWS_SAM_STACK_NAME is not set.
 */
const getAndVerifyStackName = async () => {
  const stackName = process.env["AWS_SAM_STACK_NAME"];
  if (!stackName) {
    throw new Error(
      "Cannot find env var AWS_SAM_STACK_NAME.\n" +
        "Please setup this environment variable with the stack name where we are running integration tests."
    );
  }

  const client = new AWS.CloudFormation();
  try {
    await client
      .describeStacks({
        StackName: stackName,
      })
      .promise();
  } catch (e) {
    throw new Error(
      `Cannot find stack ${stackName}: ${e.message}\n` +
        `Please make sure stack with the name "${stackName}" exists.`
    );
  }

  return stackName;
};

/**
 * This integration test will execute the step function and verify
 * - "Record Transaction" is executed
 * - the record has been inserted into the transaction record
 *
 * Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test.
 */
describe("Test State Machine", function () {
  let stateMachineArn, transactionTableName;

  let insertedRecordId;

  /**
   * Based on the provided stack name,
   * here we use cloudformation API to find out:
   * - StockTradingStateMachine's ARN
   * - TransactionTable's table name
   */
  before(async () => {
    const stackName = await getAndVerifyStackName();

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
            S: insertedRecordId,
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

    return response.executionArn;
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
  const retrieveTransactionTableInput = async (executionArn) => {
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

    const transactionTableInput = JSON.parse(
      recordTransactionEnteredEvent.stateEnteredEventDetails.input
    );
    insertedRecordId = transactionTableInput["id"]; // store the record ID for cleaning up
    return transactionTableInput;
  };

  /**
   * Use the input recorded in _retrieve_transaction_table_input() to
   * verify whether the record has been written to dynamodb
   */
  const verifyTransactionRecordWritten = async (transactionTableInput) => {
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
    const executionArn = await startExecution();
    await waitExecution(executionArn);
    const transactionTableInput = await retrieveTransactionTableInput(
      executionArn
    );
    await verifyTransactionRecordWritten(transactionTableInput);
  });
});
