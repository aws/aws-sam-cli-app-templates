import { ApiGatewayEvent } from '../common/apigateway/apigateway-event';
import { ApiGatewayResponse } from '../common/apigateway/apigateway-response';
import { TodoDynamoClientRepository } from '../common/todo-dynamoclient-repository';
import { PostApp } from '../apps/post-app';
import { LambdaApp } from '../apps/lambda-app';

/**
 * Sample Lambda function which creates an instance of a PostApp and executes it.
 * The PostApp takes the HTTP request body, turns it into a TodoItem and stores it in DynamoDB.
 * 
 * @param {Object} event - Input event to the Lambda function
 *
 * @returns {Object} object - Object containing the TodoItem stored.
 * 
 */
export const handler = async (event: ApiGatewayEvent): Promise<ApiGatewayResponse> => {
    if (!process.env['SAMPLE_TABLE']) {
        console.log('Lambda environment variables is missing the SAMPLE_TABLE variable required.');
        return { statusCode: 500 };
    }
    
    const table: string = process.env['SAMPLE_TABLE'];
    const repository = new TodoDynamoClientRepository();
    
    // We abstract all of the logic into an implementation of LambdaApp to simplify testing of the function.
    const app: LambdaApp = new PostApp(table, repository);
    
    console.log('Running the PostApp');
    return await app.run(event);
};