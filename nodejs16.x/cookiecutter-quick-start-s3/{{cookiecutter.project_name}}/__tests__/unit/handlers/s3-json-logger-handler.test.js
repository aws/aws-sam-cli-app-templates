const AWS = require('aws-sdk-mock');

describe('Test s3JsonLoggerHandler', () => {
  it('should read and log S3 objects', async () => {
    const objectBody = '{"Test": "PASS"}';
    const getObjectResp = {
      Body: objectBody
    };

    AWS.mock('S3', 'getObject', function(params, callback) {
      callback(null, getObjectResp);
    });

    const event = {
      Records: [
        {
          s3: {
            bucket: {
              name: "test-bucket"
            },
            object: {
              key: "test-key"
            }
          }
        }
      ]
    }

    console.info = jest.fn();
    let handler = require('../../../src/handlers/s3-json-logger.js');

    await handler.s3JsonLoggerHandler(event, null);

    expect(console.info).toHaveBeenCalledWith(objectBody);
    AWS.restore('S3');
  });
});
