import { ApiGatewayEvent } from '../models/apigateway/apigateway-event';
import { ApiGatewayResponse } from '../models/apigateway/apigateway-response';
import { GetByIdApp } from '../apps/get-by-id-app';
import { TodoDynamoClientRepository } from '../models/todo-dynamoclient-repository';

export const handler = async (event: ApiGatewayEvent): Promise<ApiGatewayResponse> => {
    if (!process.env['SAMPLE_TABLE']) {
        return { statusCode: 500 };
    }
    
    const table: string = process.env['SAMPLE_TABLE'];
    const repository = new TodoDynamoClientRepository();
    
    const app = new GetByIdApp(table, repository);
    return await app.run(event);
};