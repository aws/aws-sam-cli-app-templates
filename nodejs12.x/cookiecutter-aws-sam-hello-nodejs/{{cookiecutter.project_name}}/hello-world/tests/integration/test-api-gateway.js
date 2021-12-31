"use strict";

const chai = require("chai");
const AWS = require("aws-sdk");
const https = require("https");
const expect = chai.expect;

/**
 * Get stack name from environment variable AWS_SAM_STACK_NAME.
 * throw exception if AWS_SAM_STACK_NAME is not set.
 */
const getStackName = () => {
  const stackName = process.env["AWS_SAM_STACK_NAME"];
  if (!stackName) {
    throw new Error(
      "Cannot find env var AWS_SAM_STACK_NAME.\n" +
        "Please setup this environment variable with the stack name where we are running integration tests."
    );
  }

  return stackName;
};

/**
 * Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test.
 */
describe("Test API Gateway", function () {
  let apiEndpoint;

  /**
   * Based on the provided stack name,
   * here we use cloudformation API to find out what the HelloWorldApi URL is
   */
  before(async () => {
    const stackName = getStackName();

    const client = new AWS.CloudFormation();

    let response;
    try {
      response = await client
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

    const stacks = response.Stacks;

    const stackOutputs = stacks[0].Outputs;
    const apiOutput = stackOutputs.find(
      (output) => output.OutputKey === "HelloWorldApi"
    );

    expect(apiOutput, `Cannot find output HelloWorldApi in stack ${stackName}`)
      .not.to.be.undefined;

    apiEndpoint = apiOutput.OutputValue;
  });

  /**
   * Call the API Gateway endpoint and check the response
   */
  it("verifies successful response from api gateway", (done) => {
    console.info("api endpoint:", apiEndpoint);
    https
      .get(apiEndpoint, (res) => {
        expect(res.statusCode).to.be.equal(200);

        res.on("data", (data) => {
          const response = JSON.parse(data);
          expect(response).to.be.an("object");
          expect(response.message).to.be.equal("hello world");
          done();
        });
      })
      .on("error", (e) => {
        throw e;
      });
  });
});
