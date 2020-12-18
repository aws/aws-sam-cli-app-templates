import 'mocha';
import { expect } from 'chai';
import { Mock, It, Times } from 'moq.ts';

import { GetByIdApp } from '../../src/apps/get-by-id-app';
import { TodoItem } from '../../src/common/todo-item';
import { TodoRepository } from '../../src/common/todo-repository';
import { ApiGatewayResponse } from '../../src/common/apigateway/apigateway-response';

import { ApiGatewayEventMock } from '../mocks/apigateway-event-mock';

describe('PostApp instance', () => {
    const tableName = 'MY_TABLE';
    
    // Stubs out our TodoRepository interface so we can simulate the expected behavior
    // with a successful "put" to the underlying data store.
    const repoMock = new Mock<TodoRepository>()
        .setup(instance => instance.putTodo(It.IsAny(), tableName))
        .returns(new Promise<void>((resolve) => { resolve(); }));
        
    describe('constructor', () => {
        
        it('table is assigned', () => {
            const app = new GetByIdApp(tableName, repoMock.object());
            
            expect(app.table).to.equal(tableName);
        });
        
        it('repository is assigned', () => {
            const app = new GetByIdApp(tableName, repoMock.object());
            
            expect(app.repository).to.equal(repoMock.object());
        });
    });
    
    describe('run', () => {
        it('path parameter missing "id" returns 404 status code', async () => {
            const event = new ApiGatewayEventMock();
            
            const app = new GetByIdApp(tableName, repoMock.object());
            const response: ApiGatewayResponse = await app.run(event);
            
            expect(response).to.have.property('statusCode');
            expect(response.statusCode).to.equal(404);
        });
        
        it('repository is called to get a record by id', async () => {
            const todo: TodoItem = { id: '123', title: 'hello world', isComplete: true };
            
            // Stub a getById invocation resolving a Promise with a valid TodoItem
            // instance from the data store
            const mock = new Mock<TodoRepository>()
                .setup(instance => instance.getTodoById(It.IsAny(), tableName))
                .returns(new Promise<TodoItem>((resolve) => { 
                    resolve(todo);
                }));
                
            const event = new ApiGatewayEventMock();
            event.pathParameters = { id: todo.id };

            const app = new GetByIdApp(tableName, mock.object());
            const response: ApiGatewayResponse = await app.run(event);
            
            mock.verify(instance => instance.getTodoById(It.IsAny(), tableName), Times.Once());
            if (!response.body) {
                expect.fail('expected a response body to be present');
            }
            
            const responseTodo: TodoItem = JSON.parse(response.body) as TodoItem;
            expect(responseTodo.id).to.equal(todo.id);
        });
    });
});