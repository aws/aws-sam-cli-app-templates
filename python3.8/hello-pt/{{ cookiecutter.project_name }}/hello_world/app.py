from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
{%- if cookiecutter["Powertools Logging"] == "enabled"%}
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
{%- endif %}
{%- if cookiecutter["Powertools Tracing"] == "enabled"%}
from aws_lambda_powertools import Tracer
{%- endif %}
{%- if cookiecutter["Powertools Metrics"] == "enabled"%}
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit
{%- endif %}

app = APIGatewayRestResolver()
{%- if cookiecutter["Powertools Tracing"] == "enabled"%}
tracer = Tracer()
{%- endif %}
{%- if cookiecutter["Powertools Logging"] == "enabled"%}
logger = Logger()
{%- endif %}
{%- if cookiecutter["Powertools Metrics"] == "enabled"%}
metrics = Metrics(namespace="Powertools")
{%- endif %}

@app.get("/hello")
{%- if cookiecutter["Powertools Tracing"] == "enabled"%}
@tracer.capture_method
{%- endif %}
def hello():

    {%- if cookiecutter["Powertools Metrics"] == "enabled" %}
    # adding custom metrics
    # See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/
    metrics.add_metric(name="HelloWorldInvocations", unit=MetricUnit.Count, value=1)

    {%- endif %}

    {%- if cookiecutter["Powertools Logging"] == "enabled" %}

    # structured log
    # See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/logger/
    logger.info("Hello world API - HTTP 200")
    {%- endif %}
    return {"message": "hello world"}


{%- if cookiecutter["Powertools Logging"] == "enabled" %}

# Enrich logging with contextual information from Lambda
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
{%- endif %}
{%- if cookiecutter["Powertools Tracing"] == "enabled" %}
# Adding tracer
# See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/tracer/
@tracer.capture_lambda_handler
{%- endif %}
{%- if cookiecutter["Powertools Metrics"] == "enabled" %}
# ensures metrics are flushed upon request completion/failure and capturing ColdStart metric
@metrics.log_metrics(capture_cold_start_metric=True)
{%- endif %}
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
