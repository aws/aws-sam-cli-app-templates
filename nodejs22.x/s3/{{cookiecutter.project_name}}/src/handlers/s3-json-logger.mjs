import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { sdkStreamMixin } from '@aws-sdk/util-stream-node';

const s3 = new S3Client({ });

/**
 * A Lambda function that logs the payload received from S3.
 */
export const s3JsonLoggerHandler = async (event, context) => {
  // All log statements are written to CloudWatch by default. For more information, see
  // https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-logging.html
  const getObjectRequests = event.Records.map(record => {
    const params = {
      Bucket: record.s3.bucket.name,
      Key: record.s3.object.key
    };

    const getObject = new GetObjectCommand(params);

    return s3.send(getObject).then((data) => 
      sdkStreamMixin(data.Body).transformToString().then((objectString) => {
        console.info(objectString);
        return Promise.resolve(objectString);
      })
      .catch((err) => {
       console.error("Error consuming response stream:", err);
       return Promise.reject(err);
      })
      )
      .catch((err) => {
      console.error("Error calling S3 getObject:", err);
      return Promise.reject(err);
    })
  });
  
  return Promise.all(getObjectRequests).then(() => {
    console.debug('Complete!');
  });
};