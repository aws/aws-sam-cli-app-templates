// Import helloFromLambdaHandler function from hello-from-lambda.mjs
import { helloFromLambdaHandler } from '../../../src/handlers/hello-from-lambda.mjs';

// This includes all tests for helloFromLambdaHandler()
describe('Test for hello-from-lambda', function () {
    // This test invokes helloFromLambdaHandler() and compare the result 
    it('Verifies successful response', async () => {
        // Invoke helloFromLambdaHandler()
        const result = await helloFromLambdaHandler();
        /* 
            The expected result should match the return from your Lambda function.
            e.g. 
            if you change from `const message = 'Hello from Lambda!';` to `const message = 'Hello World!';` in hello-from-lambda.mjs
            you should change the following line to `const expectedResult = 'Hello World!';`
        */
        const expectedResult = 'Hello from Lambda!';
        // Compare the result with the expected result
        expect(result).toEqual(expectedResult);
    });
});
