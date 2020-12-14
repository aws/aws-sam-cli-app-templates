import { ApiGatewayEvent } from '../models/apigateway/apigateway-event';
import { ApiGatewayResponse } from '../models/apigateway/apigateway-response';

import { TodoRepository } from '../models/todo-repository';
import { TodoItem } from '../models/todo-item';

export class PostApp {
    table: string;
    repository: TodoRepository;
    
    constructor(table: string, repository: TodoRepository) {
        this.table = table;
        this.repository = repository;
    }
    
    async run(event: ApiGatewayEvent): Promise<ApiGatewayResponse> {
        
        try {
            const todo: TodoItem = JSON.parse(event.body);
            
            if (!todo.title) {
                return { statusCode: 422 };
            } else if (!todo.isComplete) {
                todo.isComplete = false;
            } else if (!todo.id) {
                return { statusCode: 422 };
            }
            
            await this.repository.putTodo(todo, this.table);
            return { statusCode: 201, body: JSON.stringify(todo) };
            
        } catch(err) {
            console.log(err.message);
            return { statusCode: 500 };
        }
    }
}