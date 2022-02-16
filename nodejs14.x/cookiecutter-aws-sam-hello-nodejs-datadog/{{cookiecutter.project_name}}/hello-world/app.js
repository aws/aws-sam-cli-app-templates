const dd_lambda = require("datadog-lambda-js");
const tracer = require("dd-trace").init();

// submit a custom span named "sleep"
const sleep = tracer.wrap("sleep", (ms) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
});

exports.lambdaHandler = async (event, context) => {
  // add custom tags to the lambda function span,
  // does NOT work when X-Ray tracing is enabled
  const span = tracer.scope().active();
  span.setTag('customer_id', '123456');

  await sleep(100);

  // submit a custom span
  const sandwich = tracer.trace('hello.world', () => {
    console.log('Hello, World!');
  });

  // submit a custom metric
  dd_lambda.sendDistributionMetric(
    "coffee_house.order_value", // metric name
    12.45, // metric value
    "product:latte", // tag
    "order:online", // another tag
  );

  const response = {
    statusCode: 200,
    body: JSON.stringify({
      message: "Hello from serverless!"
    }),
  };
  return response;
};