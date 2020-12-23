const AWS = require("aws-sdk");

/**
 * Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test.
 */
describe("Test Function Invoke", function () {
  let functionName;

  /**
   * Based on the provided env variable AWS_SAM_STACK_NAME,
   * here we use cloudformation API to find out what the helloFromLambdaFunction is
   */
  beforeAll(async () => {
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
