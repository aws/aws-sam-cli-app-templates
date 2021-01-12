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
 * This integration test creates a temporary file in the AppBucket
 * invoke the S3JsonLoggerFunction and make sure cloudwatch has corresponding log entry.
 * Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test.
 */
describe("Test S3 Logger", function () {
  let functionName, bucketName;

  let fileName;
  /**
   * Based on the provided stack name,
   * here we use cloudformation API to find out what the S3JsonLoggerFunction and AppBucket are
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
      (resource) => resource.LogicalResourceId === "S3JsonLoggerFunction"
    );
    expect(functionResource).not.toBe(undefined);

    const bucketResource = resources.find(
      (resource) => resource.LogicalResourceId === "AppBucket"
    );
    expect(bucketResource).not.toBe(undefined);

    functionName = functionResource.PhysicalResourceId;
    bucketName = bucketResource.PhysicalResourceId;
  });

  /**
   * create the temporary file, with unique file name and conetent (content is the same as file name)
   */
  beforeEach(() => {
    const testId = uuid.v4();
    fileName = `integ-test-${testId}`;

    const client = new AWS.S3();
    return client
      .putObject({
        Bucket: bucketName,
        Key: fileName,
        Body: fileName, // file content the same as file name
        Tagging: `integ-test=${testId}`,
      })
      .promise();
  });

  /**
   * clean up the temporary file
   */
  afterEach(async () => {
    const client = new AWS.S3();

    return client
      .deleteObject({
        Bucket: bucketName,
        Key: fileName,
      })
      .promise();
  });

  /**
   * Invoke S3JsonLoggerFunction so that a log entry containing the file content is sent to cloudwatch
   */
  const invokeFunction = async () => {
    const client = new AWS.Lambda();
    const response = await client
      .invoke({
        FunctionName: functionName,
        InvocationType: "Event",
        Payload: JSON.stringify({
          Records: [
            {
              s3: {
                bucket: { name: bucketName },
                object: { key: fileName },
              },
            },
          ],
        }),
      })
      .promise();

    expect(response.StatusCode).toBe(202);
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
   * pass if fileName string appears in any event message.
   */
  const checkCloudwatchLogRecorded = async () => {
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
        (event) => event.message && event.message.includes(fileName)
      );

      if (matchEvents) {
        // event found, pass
        return;
      } else {
        console.warn(
          `Cannot find matching events containing file name ${fileName}, waiting`
        );
        retries -= 1;
        await sleep(5);
      }
    }

    throw new Error(
      `Cannot find matching events containing file name ${fileName} after 5 retries`
    );
  };

  /**
   * Calling the S3JsonLoggerFunction using AWS API and
   * check the corresponding log is inserted into cloudwatch
   */
  it("When S3JsonLoggerFunction called, cloudwatch should have logs recorded", async () => {
    console.info("function name:", functionName, "bucket name:", bucketName);

    await invokeFunction();
    await checkCloudwatchLogRecorded();
  }, 60000); // timeout 60 secs, it takes some time for cloudwatch log to show up
});
