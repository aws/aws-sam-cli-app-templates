import { ApiGatewayRequestContextIdentity } from './apigateway-request-context-identity';

export interface ApiGatewayRequestContext {
    accountId: string;
    resourceId: string;
    stage: string;
    requestId: string;
    requestTime: string;
    requestTimeEpoch: number;
    path: string;
    resourcePath: string;
    httpMethod: string;
    apiId: string;
    
    identity?: ApiGatewayRequestContextIdentity;
}