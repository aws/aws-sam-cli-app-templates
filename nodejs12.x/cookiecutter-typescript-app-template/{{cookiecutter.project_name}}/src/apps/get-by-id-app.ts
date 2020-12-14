import { ApiGatewayEvent } from '../models/apigateway/apigateway-event';
import { ApiGatewayResponse } from '../models/apigateway/apigateway-response';

import { TodoRepository } from '../models/todo-repository';
import { TodoItem } from '../models/todo-item';

export class GetByIdApp {
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