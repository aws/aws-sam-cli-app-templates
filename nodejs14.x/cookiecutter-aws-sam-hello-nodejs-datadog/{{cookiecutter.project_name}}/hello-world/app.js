import { tracer } from ddtrace;
import { lambda_metric } from datadog_lambda.metric

function get_message() {
    return 'Hello from serverless!';
}

get_message = tracer.wrap(get_message);

exports.lambdaHandler = async (event, context) => {
    
    // add custom tags to the lambda function span,
    // does NOT work when X-Ray tracing is enabled
    current_span = tracer.current_span();
    if (current_span) {
        current_span.set_tag('customer.id', '123456');
    }

    // submit a custom span
    with (tracer.trace("hello.world")) {
        print('Hello, World!');
    }

    // submit a custom metric
    lambda_metric(
        metric_name='coffee_house.order_value',
        value=12.45,
        tags=['product:latte', 'order:online']
    )

    return {
        "statusCode": 200,
        'body': get_message()
    }
}

