// `awslambda` object doesn't exist outside of the Lambda runtime, so we mock its definitions here
awslambda = {
    streamifyResponse: _streamifyResponseMock,
    HttpResponseStream: { from: _responseStreamMock },
};

const { handler } = require('../../src/index.js');

// This includes all tests for handler()
describe('Test for streaming handler', function () {
    // This test invokes handler() and compare the values streamed
    it('Verifies successful response', async () => {
        const responseStream = {
            setContentType: jest.fn(),
            write: jest.fn(),
            end: jest.fn(),
        }
        // Invoke handler()
        await handler({}, responseStream);

        // Check some of the text that was streamed from your Lambda function.
        const expectedResults = ['<html>', '<p>First write!</p>', '</html>'];
        // Compare the result with the expected result
        expect(responseStream.write).toHaveBeenCalledWith(expectedResults[0]);
        expect(responseStream.write).toHaveBeenCalledWith(expectedResults[1]);
        expect(responseStream.write).toHaveBeenLastCalledWith(expectedResults[2]);
        expect(responseStream.end).toHaveBeenCalledTimes(1);
    });
});

function _streamifyResponseMock(lambdaHandler) {
    return lambdaHandler;
}

function _responseStreamMock(responseStream, httpResponseMetadata){
    responseStream.setContentType("vnd.awslambda.http-integration-response");
    responseStream.write(httpResponseMetadata);
    // Separator between metadata and the body
    responseStream.write("\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000");
    return responseStream;
}