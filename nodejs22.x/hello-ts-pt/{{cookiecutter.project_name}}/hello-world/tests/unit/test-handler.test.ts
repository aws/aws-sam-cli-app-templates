import { APIGatewayProxyEvent, APIGatewayProxyResult, Context } from 'aws-lambda';
import { lambdaHandler } from '../../app';
import { expect, describe, it } from '@jest/globals';

describe('Unit test for app handler', function () {
    it('verifies successful response', async () => {
        const event: APIGatewayProxyEvent = {
            httpMethod: 'get',
            body: '',
            headers: {},
            isBase64Encoded: false,
            multiValueHeaders: {},
            multiValueQueryStringParameters: {},
            path: '/hello',
            pathParameters: {},
            queryStringParameters: {},
            requestContext: {
                accountId: '123456789012',
                apiId: '1234',
                authorizer: {},
                httpMethod: 'get',
                identity: {
                    accessKey: '',
                    accountId: '',
                    apiKey: '',
                    apiKeyId: '',
                    caller: '',
                    clientCert: {
                        clientCertPem: '',
                        issuerDN: '',
                        serialNumber: '',
                        subjectDN: '',
                        validity: { notAfter: '', notBefore: '' },
                    },
                    cognitoAuthenticationProvider: '',
                    cognitoAuthenticationType: '',
                    cognitoIdentityId: '',
                    cognitoIdentityPoolId: '',
                    principalOrgId: '',
                    sourceIp: '',
                    user: '',
                    userAgent: '',
                    userArn: '',
                },
                path: '/hello',
                protocol: 'HTTP/1.1',
                requestId: 'c6af9ac6-7b61-11e6-9a41-93e8deadbeef',
                requestTimeEpoch: 1428582896000,
                resourceId: '123456',
                resourcePath: '/hello',
                stage: 'dev',
            },
            resource: '',
            stageVariables: {},
        };
        const context: Context = {
            callbackWaitsForEmptyEventLoop: false,
            functionName: 'lambdaHandler',
            functionVersion: '1.0',
            invokedFunctionArn: 'arn:1234567890:lambda:lambdaHandler',
            memoryLimitInMB: '128',
            awsRequestId: '1234567890',
            logGroupName: 'lambdaHandlerLogGroup',
            logStreamName: 'c6a789dff9326bc178',
            getRemainingTimeInMillis: function (): number {
                throw new Error('Function not implemented.');
            },
            done: function (error?: Error, result?: any): void {
                throw new Error('Function not implemented.');
            },
            fail: function (error: string | Error): void {
                throw new Error('Function not implemented.');
            },
            succeed: function (messageOrObject: any): void {
                throw new Error('Function not implemented.');
            }
        };
        const result: APIGatewayProxyResult = await lambdaHandler(event,context);

        expect(result.statusCode).toEqual(200);
        expect(result.body).toEqual(
            JSON.stringify({
                message: 'hello world',
            }),
        );
    });
});
