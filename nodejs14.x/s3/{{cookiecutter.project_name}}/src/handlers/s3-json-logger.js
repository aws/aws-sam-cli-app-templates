const AWS = require('aws-sdk');

const s3 = new AWS.S3();

/**
 * A Lambda function that logs the payload received from S3.
 */
exports.s3JsonLoggerHandler = async (event, context) => {
  // All log statements are written to CloudWatch by default. For more information, see
  // https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-logging.html
  const getObjectRequests = event.Records.map(record => {
    const params = {
      Bucket: record.s3.bucket.name,
      Key: record.s3.object.key
    };
    return s3.getObject(params).promise().then(data => {
      console.info(data.Body.toString());
    }).catch(err => {
      console.error("Error calling S3 getObject:", err);
      return Promise.reject(err);
    })
  });
  return Promise.all(getObjectRequests).then(() => {
    //console.debug('Complete!');
  });
};
