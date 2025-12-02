import json
from typing import Any

from aws_durable_execution_sdk_python.context import DurableContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution
from aws_durable_execution_sdk_python.types import StepContext


@durable_step
def say_hello(step_context: StepContext, name: str) -> str:
    """Durable step that generates a greeting message."""
    step_context.logger.info("Generating greeting for: %s", name)
    return f"Hello, {name}!"


@durable_execution
def lambda_handler(event: Any, context: DurableContext) -> dict[str, Any]:
    """Durable Lambda function handler.

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

    context: DurableContext, required
        Durable execution context

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict
    """
    context.logger.info("Starting durable hello world execution")

    # Execute durable step
    message = context.step(say_hello(name="World"))

    context.logger.info("Execution completed successfully")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        }),
    }
