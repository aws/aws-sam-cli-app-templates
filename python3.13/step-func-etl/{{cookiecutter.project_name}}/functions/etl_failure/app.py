def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        Choice output

        {
            "JobName": "your_job_name",
            "JobRunId": "jr_uuid",
            "JobRunState": "FAILED",
            "StartedOn": "2021-09-20T20:30:55.389000+00:00",
            "CompletedOn": "2021-09-20T20:32:51.443000+00:00",
            "ExecutionTime": 106
        }

    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    Final status of the execution
    """
    output = {
        "message": "failed glue job execution"
    }
    return output
