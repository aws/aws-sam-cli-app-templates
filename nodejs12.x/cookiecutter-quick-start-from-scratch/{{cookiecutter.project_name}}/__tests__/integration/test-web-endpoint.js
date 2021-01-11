const AWS = require("aws-sdk");

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
 * Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test.
 */
describe("Test Function Invoke", function () {
  let functionName;

  /**
   * Based on the provided stack name,
   * here we use cloudformation API to find out what the helloFromLambdaFunction is
   */
  beforeAll(async () => {
    const stackName = await getAndVerifyStackName();

    const client = new AWS.CloudFormation();
    const response = await client
      .listStackResources({
        StackName: stackName,
      })
      .promise();

    const resources = response.StackResourceSummaries;

    const functionResource = resources.find(
      (resource) => resource.LogicalResourceId === "helloFromLambdaFunction"
    );
    expect(functionResource).not.toBe(undefined);

    functionName = functionResource.PhysicalResourceId;
  });

  /**
   * Calling the helloFromLambdaFunction using AWS API
   */
  it("helloFromLambdaFunction should be invokable", async () => {
    console.info("function name:", functionName);

    const client = new AWS.Lambda();
    const response = await client
      .invoke({
        FunctionName: functionName,
        Payload: "{}",
      })
      .promise();

    expect(response.StatusCode).toBe(200);
    expect(response.Payload.toString()).toBe(
      JSON.stringify("Hello from Lambda!")
    );
  });
});
