import { lambdaHandler } from './app';
import { APIGatewayProxyEvent } from 'aws-lambda';
import { LocalDurableTestRunner } from '@aws/durable-execution-sdk-js-testing';

describe('Tests for durable hello world handler', () => {
    beforeAll(() => LocalDurableTestRunner.setupTestEnvironment({ skipTime: true }));
    afterAll(() => LocalDurableTestRunner.teardownTestEnvironment());

    let runner: LocalDurableTestRunner<any>;

    beforeEach(() => {
        runner = new LocalDurableTestRunner({ handlerFunction: lambdaHandler });
    });

    it('verifies successful response', async () => {
        const event: APIGatewayProxyEvent = {
            httpMethod: 'GET',
            path: '/hello',
        } as APIGatewayProxyEvent;

        const execution = await runner.run({ payload: event });
        const result = execution.getResult();

        expect(result.statusCode).toEqual(200);
        expect(result.body).toBeDefined();
        
        const body = JSON.parse(result.body);
        expect(body.message).toEqual('Hello, World!');
    });
});
