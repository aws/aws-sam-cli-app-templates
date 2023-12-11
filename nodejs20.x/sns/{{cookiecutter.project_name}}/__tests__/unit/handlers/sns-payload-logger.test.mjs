// Import snsPayloadLoggerHandler function from sns-payload-logger.mjs
import { snsPayloadLoggerHandler } from '../../../src/handlers/sns-payload-logger.mjs';
import { jest } from '@jest/globals'

describe('Test for sns-payload-logger', function () {
    // This test invokes the sns-payload-logger Lambda function and verifies that the received payload is logged
    it('Verifies the payload is logged', async() => {
        // Mock console.log statements so we can verify them. For more information, see
        // https://jestjs.io/docs/en/mock-functions.html
        console.info = jest.fn()

        // Create a sample payload with SNS message format
        var payload = {
            TopicArn: "arn:aws:sns:us-west-2:123456789012:SimpleTopic",
            Message: "This is a notification from SNS",
            Subject: "SNS Notification"
        }

        await snsPayloadLoggerHandler(payload, null)

        // Verify that console.info has been called with the expected payload
        expect(console.info).toHaveBeenCalledWith(payload)
    });
});
