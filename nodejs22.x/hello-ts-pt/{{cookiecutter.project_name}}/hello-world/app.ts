import { APIGatewayProxyEvent, APIGatewayProxyResult, Context } from 'aws-lambda';
{%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Metrics"] == "enabled"%}
import { Metrics } from '@aws-lambda-powertools/metrics';
{%- endif %}
{%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Logging"] == "enabled"%}
import { Logger } from '@aws-lambda-powertools/logger';
{%- endif %}
{%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Tracing"] == "enabled"%}
import { Tracer } from '@aws-lambda-powertools/tracer';
{%- endif %}


{%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Metrics"] == "enabled"%}
const metrics = new Metrics();
{%- endif %}
{%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Logging"] == "enabled"%}
const logger = new Logger();
{%- endif %}
{%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Tracing"] == "enabled"%}
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

    {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Logging"] == "enabled"%}

    // Log the incoming event
    logger.info('Lambda invocation event', { event });

    // Append awsRequestId to each log statement
    logger.appendKeys({
        awsRequestId: context.awsRequestId,
    });

    {%- endif %}

    {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Tracing"] == "enabled"%}
    // Get facade segment created by AWS Lambda
    const segment = tracer.getSegment();

    if (!segment) {
        response = {
            statusCode: 500,
            body: "Failed to get segment"
        }
        return response;
    }

    // Create subsegment for the function & set it as active
    const handlerSegment = segment.addNewSubsegment(`## ${process.env._HANDLER}`);
    tracer.setSegment(handlerSegment);

    // Annotate the subsegment with the cold start & serviceName
    tracer.annotateColdStart();
    tracer.addServiceNameAnnotation();

    // Add annotation for the awsRequestId
    tracer.putAnnotation('awsRequestId', context.awsRequestId);

    {%- endif %}
    {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Metrics"] == "enabled" %}
    // Capture cold start metrics
    metrics.captureColdStartMetric();

    {%- endif %}
    {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Tracing"] == "enabled"%}
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
        {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Logging"] == "enabled"%}
        logger.info(`Successful response from API enpoint: ${event.path}`, response.body);
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
        {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Tracing"] == "enabled"%}
        tracer.addErrorAsMetadata(err as Error);
        {%- endif %}

        {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Logging"] == "enabled"%}
        logger.error(`Error response from API enpoint: ${err}`, response.body);
        {%- else %}
        console.log('sending HTTP 500 - some error happened response')
        {%- endif %}
    {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Metrics"] == "enabled" or cookiecutter["Powertools for AWS Lambda (TypeScript) Tracing"] == "enabled"%}
    } finally {
        {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Tracing"] == "enabled"%}
        // Close subsegments (the AWS Lambda one is closed automatically)
        subsegment.close(); // (### MySubSegment)
        handlerSegment.close(); // (## index.handler)

        // Set the facade segment as active again (the one created by AWS Lambda)
        tracer.setSegment(segment);

        {%- endif %}
        {%- if cookiecutter["Powertools for AWS Lambda (TypeScript) Metrics"] == "enabled"%}
        // Publish all stored metrics
        metrics.publishStoredMetrics();

        {%- endif %}
    {%- endif %}
    }

    return response;

};