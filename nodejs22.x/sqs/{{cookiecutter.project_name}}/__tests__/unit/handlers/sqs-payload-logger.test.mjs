// Import sqsPayloadLoggerHandler function from sqs-payload-logger.mjs
import { sqsPayloadLoggerHandler } from '../../../src/handlers/sqs-payload-logger.mjs';
import { jest } from '@jest/globals';

describe('Test for sqs-payload-logger', function () {
    // This test invokes the sqs-payload-logger Lambda function and verifies that the received payload is logged
    it('Verifies the payload is logged', async () => {
        // Mock console.log statements so we can verify them. For more information, see
        // https://jestjs.io/docs/en/mock-functions.html
        console.info = jest.fn()

        // Create a sample payload with SQS message format
        var payload = {
            DelaySeconds: 10,
            MessageAttributes: {
                "Sender": {
                    DataType: "String",
                    StringValue: "sqs-payload-logger"
                }
            },
            MessageBody: "This message was sent by the sqs-payload-logger Lambda function",
            QueueUrl: "SQS_QUEUE_URL"
        }

        await sqsPayloadLoggerHandler(payload, null)

        // Verify that console.info has been called with the expected payload
        expect(console.info).toHaveBeenCalledWith(JSON.stringify(payload))
    });
});
