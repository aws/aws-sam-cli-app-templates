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
    
    async getById(id: string, table: string): Promise<TodoItem> {
        
        const params: DynamoDB.DocumentClient.GetItemInput = {
            TableName: table,
            Key: {
                "id": id
            }
        };
        
        const result: DynamoDB.DocumentClient.GetItemOutput = await this.docClient.get(params).promise();
        return result.Item as TodoItem;
    }
}