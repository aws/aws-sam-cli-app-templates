import { mockClient } from 'aws-sdk-client-mock';
import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { s3JsonLoggerHandler } from '../../../src/handlers/s3-json-logger.mjs';
import { jest } from '@jest/globals';
import { Readable } from 'stream';

describe('Test s3JsonLoggerHandler', () => {
  const s3Mock = mockClient(S3Client);

  beforeEach(() => {
    s3Mock.reset();
  });

  it('should read and log S3 objects', async () => {
    const objectBody = '{"Test": "PASS"}';
    const getObjectResp = {
      data: objectBody
    };

    const s3ResponseStream = new Readable({
      read() {}
    });

    s3ResponseStream.push(objectBody);
    s3ResponseStream.push(null);

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

    s3Mock.on(GetObjectCommand).resolves({
      Body: s3ResponseStream
    });

    console.info = jest.fn()

    await s3JsonLoggerHandler(event, null);

    expect(console.info).toHaveBeenCalledWith(objectBody);
  });
});
