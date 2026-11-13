import json
import pytest
from functions.etl_success import app as etl_success
from functions.etl_failure import app as etl_failure

@pytest.fixture()
def glue_event():
    """ Generates Glue Event"""

    return {
        "JobName": "your_job_name",
        "JobRunId": "jr_uuid",
        "JobRunState": "SUCCEEDED",
        "StartedOn": "2021-09-20T21:06:06.603000+00:00",
        "CompletedOn": "2021-09-20T21:07:53.818000+00:00",
        "ExecutionTime": 94
        }

def test_lambda_handler(glue_event, mocker):
    response = etl_success.lambda_handler(glue_event, "")
    assert response["message"] == "successful glue job execution"
    response = etl_failure.lambda_handler(glue_event, "")
    assert response["message"] == "failed glue job execution"
