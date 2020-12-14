import { ApiGatewayEvent } from '../common/apigateway/apigateway-event';
import { ApiGatewayResponse } from '../common/apigateway/apigateway-response';

export interface LambdaApp {
    run(event: ApiGatewayEvent): Promise<ApiGatewayResponse>;
}