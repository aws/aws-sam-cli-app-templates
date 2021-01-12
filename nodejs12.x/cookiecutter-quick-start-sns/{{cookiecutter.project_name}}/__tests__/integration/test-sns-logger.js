const AWS = require("aws-sdk");
const uuid = require("uuid");

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
 * This test publish a testing message to sns topic
 * and make sure cloudwatch has corresponding log entry.
 * Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test.
 */
describe("Test SNS Logger", function () {
  let functionName, topicArn;
  /**
   * Based on the provided stack name,
   * here we use cloudformation API to find out what the SNSPayloadLogger and SimpleTopic are
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
      (resource) => resource.LogicalResourceId === "SNSPayloadLogger"
    );
    expect(functionResource).not.toBe(undefined);

    const topicResource = resources.find(
      (resource) => resource.LogicalResourceId === "SimpleTopic"
    );
    expect(topicResource).not.toBe(undefined);

    functionName = functionResource.PhysicalResourceId;
    topicArn = topicResource.PhysicalResourceId;
  });

  /**
   * Publish a SNS message so that a log entry containing the integTestId is sent to cloudwatch
   */
  const publishMessage = (integTestId) => {
    const client = new AWS.SNS();
    return client
      .publish({
        Subject: `IntegTest: ${integTestId}`,
        Message: `integ-test-${integTestId}`,
        TopicArn: topicArn,
      })
      .promise();
  };

  /**
   * find the latest log stream name, if the log group does not exist, return null.
   */
  const getLatestLogStreamName = async (logGroupName) => {
    const client = new AWS.CloudWatchLogs();
    try {
      const response = await client
        .describeLogStreams({
          logGroupName,
          orderBy: "LastEventTime",
          descending: true,
        })
        .promise();
      return response.logStreams[0].logStreamName;
    } catch (e) {
      if (e.code == "ResourceNotFoundException") {
        return null;
      }
      throw e;
    }
  };

  /**
   * Constantly check cloudwatch log group's latest log stream,
   * pass if integTestId string appears in any event message.
   */
  const checkCloudwatchLogRecorded = async (integTestId) => {
    const logGroupName = `/aws/lambda/${functionName}`;
    const client = new AWS.CloudWatchLogs();

    let retries = 5;
    const startTime = Date.now() - 60 * 1000; // we only look for log entries since 1 min ago
    while (retries >= 0) {
      const logStreamName = await getLatestLogStreamName(logGroupName);
      if (!logStreamName) {
        console.warn(`Cannot find log group ${logStreamName}, waiting`);
        await sleep(5);
        continue;
      }

      const response = await client
        .getLogEvents({
          logGroupName,
          logStreamName,
          startTime,
          endTime: Date.now(),
          startFromHead: true,
        })
        .promise();

      const matchEvents = response.events.find(
        (event) => event.message && event.message.includes(integTestId)
      );

      if (matchEvents) {
        // event found, pass
        return;
      } else {
        console.warn(
          `Cannot find matching events containing integration test id ${integTestId}, waiting`
        );
        retries -= 1;
        await sleep(5);
      }
    }

    throw new Error(
      `Cannot find matching events containing integration test id ${integTestId} after 5 retries`
    );
  };

  /**
   * Publish a message containing a unique string to the SNS topic using AWS API and
   * check the corresponding log is inserted into cloudwatch
   */
  it("When SNSPayloadLogger called, cloudwatch should have logs recorded", async () => {
    console.info("function name:", functionName, "sns topic:", topicArn);

    // we will use this uuid to verify the recorded log entry is init from this test
    const integTestId = uuid.v4();

    await publishMessage(integTestId);
    await checkCloudwatchLogRecorded(integTestId);
  }, 60000); // timeout 60 secs, it takes some time for cloudwatch log to show up
});
