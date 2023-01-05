import { ApiGatewayEvent } from '../common/apigateway/apigateway-event';
import { ApiGatewayResponse } from '../common/apigateway/apigateway-response';
import { TodoRepository } from '../common/todo-repository';
import { TodoItem } from '../common/todo-item';

import { LambdaApp } from './lambda-app';

/**
 * PostApp is a LambdaApp that puts a new record into DynamoDB using the API Gateway event body as the record content.
 * 
 */
export class PostApp implements LambdaApp {
    table: string;
    repository: TodoRepository;
    
    constructor(table: string, repository: TodoRepository) {
        this.table = table;
        this.repository = repository;
    }
    
    async run(event: ApiGatewayEvent): Promise<ApiGatewayResponse> {
        let todo: TodoItem
        try {
            todo = JSON.parse(event.body);
            if (!todo.title) {
                console.log('Body is missing the title');
                return { statusCode: 422 };
            } else if (!todo.isComplete) {
                todo.isComplete = false;
            } else if (!todo.id) {
                console.log('Body is missing the id');
                return { statusCode: 422 };
            }
        } catch (err) {
            console.log('Event body could not be parsed as JSON');
            return { statusCode: 400 };
        }

        try {
            await this.repository.putTodo(todo, this.table);
            return { statusCode: 201, body: JSON.stringify(todo) };
        } catch(err) {
            console.log(err.message);
            return { statusCode: 500 };
        }
    }
}