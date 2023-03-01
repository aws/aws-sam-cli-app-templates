import type { APIGatewayProxyEvent, Context } from 'aws-lambda';
import { handler as getAllItemsHandler } from '../src/get-all-items';
import { handler as getByIdHandler } from '../src/get-by-id';
import { handler as putItemHandler } from '../src/put-item';

test('getAllItemsHandler function imports & throws correctly', () => {
  expect(getAllItemsHandler({} as APIGatewayProxyEvent, {} as Context)).rejects.toThrow(
    'getAllItems only accepts GET method, you tried: undefined'
  );
});

test('getByIdHandler function imports & throws correctly', () => {
  expect(getByIdHandler({} as APIGatewayProxyEvent, {} as Context)).rejects.toThrow(
    'getById only accepts GET method, you tried: undefined'
  );
});

test('putItemHandler function imports & throws correctly', () => {
  expect(putItemHandler({} as APIGatewayProxyEvent, {} as Context)).rejects.toThrow(
    'putItem only accepts POST method, you tried: undefined'
  );
});