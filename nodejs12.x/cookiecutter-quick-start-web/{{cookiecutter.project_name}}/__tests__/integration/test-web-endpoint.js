const AWS = require("aws-sdk");
const https = require("https");

describe("Test Web Endpoint", function () {
  let apiEndpoint;
  /**
   * Based on the provided env variable AWS_SAM_STACK_NAME,
   * here we use cloudformation API to find out what the WebEndpoint URL is
   */
  beforeAll(async () => {
    const stackName = process.env["AWS_SAM_STACK_NAME"];
    if (!stackName) {
      throw new Error("Cannot find env var AWS_SAM_STACK_NAME");
    }

    const client = new AWS.CloudFormation();
    const response = await client
      .describeStacks({
        StackName: stackName,
      })
      .promise();

    const stacks = response.Stacks;
    expect(stacks).not.toBe(undefined);
    expect(stacks).not.toBe([]);

    const stackOutputs = stacks[0].Outputs;
    const apiOutput = stackOutputs.find(
      (output) => output.OutputKey === "WebEndpoint"
    );

    expect(apiOutput).not.toBe(undefined);

    apiEndpoint = apiOutput.OutputValue;
  });

  /**
   * Call the API Gateway endpoint GET /, the response should be an array
   */
  it("GET / should respond with an array of items", (done) => {
    console.info("api endpoint:", apiEndpoint);
    https
      .get(apiEndpoint, (res) => {
        expect(res.statusCode).toBe(200);

        res.on("data", (data) => {
          const response = JSON.parse(data);
          expect(response).toBeInstanceOf(Array);
          done();
        });
      })
      .on("error", (e) => {
        throw e;
      });
  });
});
