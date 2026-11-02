"""Unit tests for hello world durable function."""

import json

import pytest
from aws_durable_execution_sdk_python.execution import InvocationStatus
from aws_durable_execution_sdk_python_testing.runner import DurableFunctionTestRunner

from hello_world import app


@pytest.fixture
def durable_runner():
    """Create a test runner for the durable function."""
    with DurableFunctionTestRunner(handler=app.lambda_handler) as runner:
        yield runner


def test_lambda_handler_success(durable_runner):
    """Test successful execution of the durable function."""
    result = durable_runner.run(input={}, timeout=10)

    assert result.status is InvocationStatus.SUCCEEDED
    
    response = json.loads(result.result)
    assert response["statusCode"] == 200
    
    body = json.loads(response["body"])
    assert body["message"] == "Hello, World!"
    
    # Verify the step executed correctly
    step_result = result.get_step("say_hello")
    assert json.loads(step_result.result) == "Hello, World!"

