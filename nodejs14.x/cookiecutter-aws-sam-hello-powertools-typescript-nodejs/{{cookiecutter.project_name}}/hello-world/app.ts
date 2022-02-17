import { APIGatewayProxyEvent, APIGatewayProxyResult, Context } from 'aws-lambda';
import { Metrics, MetricUnits } from '@aws-lambda-powertools/metrics';
import { Logger } from '@aws-lambda-powertools/logger';
import { Tracer } from '@aws-lambda-powertools/tracer';

const namespace = 'CDKExample';
const serviceName = 'MyFunctionWithStandardHandler';

const metrics = new Metrics({ namespace: namespace, serviceName: serviceName });
const logger = new Logger({ logLevel: 'INFO', serviceName: serviceName });
const tracer = new Tracer({ serviceName: serviceName });

/**
 *
 * Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
 * @param {APIGatewayProxyEvent} event - API Gateway Lambda Proxy Input Format
 * @param {Context} object - API Gateway Lambda $context variable
 *
 * Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
 * @returns {APIGatewayProxyResult} object - API Gateway Lambda Proxy Output Format
 *
 */

export const lambdaHandler = async (event: APIGatewayProxyEvent, context: Context): Promise<APIGatewayProxyResult> => {
    let response: APIGatewayProxyResult;

    // Get facade segment created by AWS Lambda
    const segment = tracer.getSegment();

    // Create subsegment for the function & set it as active
    const handlerSegment = segment.addNewSubsegment(`## ${process.env._HANDLER}`);
    tracer.setSegment(handlerSegment);

    // Annotate the subsegment with the cold start & serviceName
    tracer.annotateColdStart();
    tracer.addServiceNameAnnotation();

    // Add annotation for the awsRequestId
    tracer.putAnnotation('awsRequestId', context.awsRequestId);

    // Capture cold start metrics
    metrics.captureColdStartMetric();

    // Create another subsegment & set it as active
    const subsegment = handlerSegment.addNewSubsegment('### MySubSegment');
    tracer.setSegment(subsegment);

    try {
        // hello world code
        response = {
            statusCode: 200,
            body: JSON.stringify({
                message: 'hello world',
            }),
        };
        logger.info('This is an INFO log - sending HTTP 200 - hello world response');

    } catch (err) {
        // Error handling
        console.log(err);
        response = {
            statusCode: 500,
            body: JSON.stringify({
                message: 'some error happened',
            }),
        };
        logger.error('This is an ERROR log - sending HTTP 500 - some error happened response');

    } finally {
        // Close subsegments (the AWS Lambda one is closed automatically)
        subsegment.close(); // (### MySubSegment)
        handlerSegment.close(); // (## index.handler)

        // Set the facade segment as active again (the one created by AWS Lambda)
        tracer.setSegment(segment);

        // Publish all stored metrics
        metrics.publishStoredMetrics();
    }

    return response;

};