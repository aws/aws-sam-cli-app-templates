from unittest import skip
from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_go1_x_cookiecutter_aws_sam_hello_golang(UnitTestBase.GoUnitTestBase):
    directory = "go1.x/cookiecutter-aws-sam-hello-golang"
    code_directories = ["hello-world"]

class UnitTest_go1_x_cookiecutter_aws_sam_eventbridge_hello_golang(UnitTestBase.GoUnitTestBase):
    directory = "go1.x/cookiecutter-aws-sam-eventbridge-hello-golang"
    code_directories = ["hello-world"]

@skip("eventbridge schema app requires credential to pull missing files, skip")
class UnitTest_go1_x_cookiecutter_aws_sam_eventbridge_schema_app_golang(UnitTestBase.GoUnitTestBase):
    directory = "go1.x/cookiecutter-aws-sam-eventbridge-schema-app-golang"
    code_directories = ["hello-world"]

class UnitTest_go1_x_cookiecutter_aws_sam_hello_step_functions_sample_app(UnitTestBase.GoUnitTestBase):
    directory = "go1.x/cookiecutter-aws-sam-hello-step-functions-sample-app"
    code_directories = ["functions/stockBuyer", "functions/stockChecker", "functions/stockSeller"]
