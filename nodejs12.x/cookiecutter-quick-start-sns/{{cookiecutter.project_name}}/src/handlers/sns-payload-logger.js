/**
 * A Lambda function that logs the payload received from SNS.
 */
exports.snsPayloadLoggerHandler = async (event, context) => {
    // All log statements are written to CloudWatch by default. For more information, see
    // https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-logging.html
    console.info(JSON.stringify(event)); // event is a deep object, JSON.stringify retains its deep property values
}
