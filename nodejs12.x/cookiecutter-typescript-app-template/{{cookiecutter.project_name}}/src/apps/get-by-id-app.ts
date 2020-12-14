import { ApiGatewayEvent } from '../common/apigateway/apigateway-event';
import { ApiGatewayResponse } from '../common/apigateway/apigateway-response';
import { TodoRepository } from '../common/todo-repository';
import { TodoItem } from '../common/todo-item';

import { LambdaApp } from './lambda-app';

export class GetByIdApp implements LambdaApp {
    table: string;
    repository: TodoRepository;
    
    constructor(table: string, repository: TodoRepository) {
        this.table = table;
        this.repository = repository;
    }
    
    async run(event: ApiGatewayEvent): Promise<ApiGatewayResponse> {

        try {
            if (!event.pathParameters?.id) {
                return { statusCode: 404 };
            }
            
            const id: string = event.pathParameters.id;
            const results: TodoItem = await this.repository.getById(id, this.table);
            
            return { statusCode: 201, body: JSON.stringify(results) };
            
        } catch(err) {
            console.log(err.message);
            return { statusCode: 500 };
        }
    }
}