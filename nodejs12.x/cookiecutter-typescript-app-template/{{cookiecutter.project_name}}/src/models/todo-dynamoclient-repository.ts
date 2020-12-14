import { DynamoDB } from 'aws-sdk';

import { TodoItem } from './todo-item';
import { TodoRepository } from './todo-repository';

export class TodoDynamoClientRepository implements TodoRepository {
    docClient: DynamoDB.DocumentClient;
    
    constructor() {
        this.docClient = new DynamoDB.DocumentClient();
    }
    
    async putTodo(todoItem: TodoItem, table: string): Promise<void> {

        const params: DynamoDB.DocumentClient.PutItemInput = {
            TableName: table,
            Item: todoItem
        };
        
        await this.docClient.put(params).promise();
        return;
    }
}