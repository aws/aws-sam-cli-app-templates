import { ApiGatewayEvent } from '../common/apigateway/apigateway-event';
import { ApiGatewayResponse } from '../common/apigateway/apigateway-response';

/**
 * Interface for function logic to be implemented behind for improved testability.
 * 
 * 
 */
export interface LambdaApp {
    run(event: ApiGatewayEvent): Promise<ApiGatewayResponse>;
}