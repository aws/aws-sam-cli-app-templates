import { withDurableExecution, DurableContext } from '@aws/durable-execution-sdk-js';
import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';

/**
 * Durable Lambda function handler.
 */
export const lambdaHandler = withDurableExecution(async (event: APIGatewayProxyEvent, context: DurableContext): Promise<APIGatewayProxyResult> => {
    context.logger.info('Starting durable hello world execution');

    // Execute durable step
    const message = await context.step(async () => {
        context.logger.info('Generating greeting for: World');
        return 'Hello, World!';
    });

    context.logger.info('Execution completed successfully');

    return {
        statusCode: 200,
        body: JSON.stringify({
            message: message,
        }),
    };
});
