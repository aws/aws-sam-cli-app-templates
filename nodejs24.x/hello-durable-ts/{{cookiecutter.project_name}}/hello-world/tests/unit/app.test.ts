import { lambdaHandler } from '../../app';
import { APIGatewayProxyEvent } from 'aws-lambda';
import { LocalDurableTestRunner, OperationType, OperationStatus } from '@aws/durable-execution-sdk-js-testing';

describe('Tests for durable hello world handler', () => {
    beforeAll(() => LocalDurableTestRunner.setupTestEnvironment({ skipTime: true }));
    afterAll(() => LocalDurableTestRunner.teardownTestEnvironment());

    it('verifies successful response', async () => {
        const runner = new LocalDurableTestRunner({ handlerFunction: lambdaHandler });
        const event: APIGatewayProxyEvent = {
            httpMethod: 'GET',
            path: '/hello',
        } as APIGatewayProxyEvent;

        const execution = await runner.run({ payload: event });
        const result = execution.getResult();

        expect(result.statusCode).toEqual(200);
        const body = JSON.parse(result.body);
        expect(body.message).toEqual('Hello, World!');

        // Verify durable execution recorded one step operation
        const operations = execution.getOperations();
        expect(operations).toHaveLength(1);

        const stepOperation = runner.getOperationByIndex(0);
        expect(stepOperation.getType()).toBe(OperationType.STEP);
        expect(stepOperation.getStatus()).toBe(OperationStatus.SUCCEEDED);
    });
});
