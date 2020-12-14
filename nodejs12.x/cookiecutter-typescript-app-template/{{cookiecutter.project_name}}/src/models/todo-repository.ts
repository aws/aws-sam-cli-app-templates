import { TodoItem } from './todo-item';

export interface TodoRepository {
    putTodo(todoItem: TodoItem, table: string): Promise<void>;
}