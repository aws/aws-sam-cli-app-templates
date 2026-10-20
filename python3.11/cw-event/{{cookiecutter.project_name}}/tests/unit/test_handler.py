import json
import logging

import pytest

from scheduled_event_logger import app


@pytest.fixture()
def scheduled_event():
    """ Generates EventBridge Scheduled Event"""

    return {
        "id": "cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
        "detail-type": "Scheduled Event",
        "source": "aws.events",
        "account": "123456789012",
        "time": "1970-01-01T00:00:00Z",
        "region": "us-west-2",
        "resources": ["arn:aws:events:us-west-2:123456789012:rule/ExampleRule"],
        "detail": {},
    }


def test_lambda_handler(scheduled_event, caplog):

    caplog.set_level(logging.INFO)

    ret = app.lambda_handler(scheduled_event, "")

    assert ret is None
    assert json.dumps(scheduled_event) in caplog.text
