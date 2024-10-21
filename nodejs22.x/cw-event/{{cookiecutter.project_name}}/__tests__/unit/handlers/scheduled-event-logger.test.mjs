// Import scheduledEventLoggerHandler function from scheduled-event-logger.mjs
import { scheduledEventLoggerHandler } from '../../../src/handlers/scheduled-event-logger.mjs';
import { jest } from '@jest/globals';

describe('Test for sqs-payload-logger', function () {
  // This test invokes the scheduled-event-logger Lambda function and verifies that the received payload is logged
  it('Verifies the payload is logged', async () => {
    // Mock console.log statements so we can verify them. For more information, see
    // https://jestjs.io/docs/en/mock-functions.html
    console.info = jest.fn()

    // Create a sample payload with CloudWatch scheduled event message format
    var payload = {
      "id": "cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
      "detail-type": "Scheduled Event",
      "source": "aws.events",
      "account": "",
      "time": "1970-01-01T00:00:00Z",
      "region": "us-west-2",
      "resources": [
        "arn:aws:events:us-west-2:123456789012:rule/ExampleRule"
      ],
      "detail": {}
    }

    await scheduledEventLoggerHandler(payload, null)

    // Verify that console.info has been called with the expected payload
    expect(console.info).toHaveBeenCalledWith(JSON.stringify(payload))
  });
});
