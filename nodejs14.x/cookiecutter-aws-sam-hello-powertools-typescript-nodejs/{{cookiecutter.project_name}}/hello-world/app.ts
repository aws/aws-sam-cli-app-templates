import { APIGatewayProxyEvent, APIGatewayProxyResult, Context } from 'aws-lambda';
{%- if cookiecutter["Powertools Metrics"] == "enabled"%}
import { Metrics, MetricUnits } from '@aws-lambda-powertools/metrics';
{%- endif %}
{%- if cookiecutter["Powertools Logging"] == "enabled"%}
import { Logger } from '@aws-lambda-powertools/logger';
{%- endif %}
{%- if cookiecutter["Powertools X-Ray Tracing"] == "enabled"%}
import { Tracer } from '@aws-lambda-powertools/tracer';
{%- endif %}


{%- if cookiecutter["Powertools Metrics"] == "enabled"%}
const metrics = new Metrics();
{%- endif %}
{%- if cookiecutter["Powertools Logging"] == "enabled"%}
const logger = new Logger();
{%- endif %}
{%- if cookiecutter["Powertools X-Ray Tracing"] == "enabled"%}
const tracer = new Tracer();
{%- endif %}

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

    {%- if cookiecutter["Powertools X-Ray Tracing"] == "enabled"%}
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

    {%- endif %}
    {%- if cookiecutter["Powertools Metrics"] == "enabled" %}
    // Capture cold start metrics
    metrics.captureColdStartMetric();

    {%- endif %}
    {%- if cookiecutter["Powertools X-Ray Tracing"] == "enabled"%}
    // Create another subsegment & set it as active
    const subsegment = handlerSegment.addNewSubsegment('### MySubSegment');
    tracer.setSegment(subsegment);

    {%- endif %}
    try {
        // hello world code
        response = {
            statusCode: 200,
            body: JSON.stringify({
                message: 'hello world',
            }),
        };
        {%- if cookiecutter["Powertools Logging"] == "enabled"%}
        logger.info('This is an INFO log - sending HTTP 200 - hello world response');
        {%- else %}
        console.log('sending HTTP 200 - hello world response')
        {%- endif %}
    } catch (err) {
        // Error handling
        response = {
            statusCode: 500,
            body: JSON.stringify({
                message: 'some error happened',
            }),
        };
        {%- if cookiecutter["Powertools Logging"] == "enabled"%}
        logger.error('This is an ERROR log - sending HTTP 500 - some error happened response');
        {%- else %}
        console.log('sending HTTP 500 - some error happened response')
        {%- endif %}
    {%- if cookiecutter["Powertools Metrics"] == "enabled" or cookiecutter["Powertools X-Ray Tracing"] == "enabled"%}
    } finally {
        {%- if cookiecutter["Powertools X-Ray Tracing"] == "enabled"%}
        // Close subsegments (the AWS Lambda one is closed automatically)
        subsegment.close(); // (### MySubSegment)
        handlerSegment.close(); // (## index.handler)

        // Set the facade segment as active again (the one created by AWS Lambda)
        tracer.setSegment(segment);

        {%- endif %}
        {%- if cookiecutter["Powertools Metrics"] == "enabled"%}
        // Publish all stored metrics
        metrics.publishStoredMetrics();

        {%- endif %}
    {%- endif %}
    }

    return response;

};