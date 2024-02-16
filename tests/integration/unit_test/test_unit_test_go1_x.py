from unittest import skip
from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_provided_go_cookiecutter_aws_sam_hello_golang(UnitTestBase.GoUnitTestBase):
    directory = "al2/go/hello"
    code_directories = ["hello-world"]

class UnitTest_providedal2023_go_cookiecutter_aws_sam_hello_golang(UnitTestBase.GoUnitTestBase):
    directory = "al2023/go/hello"
    code_directories = ["hello-world"]

class UnitTest_provided_go_cookiecutter_aws_sam_eventbridge_hello_golang(UnitTestBase.GoUnitTestBase):
    directory = "al2/go/event-bridge"
    code_directories = ["hello-world"]

@skip("eventbridge schema app requires credential to pull missing files, skip")
class UnitTest_provided_go_cookiecutter_aws_sam_eventbridge_schema_app_golang(UnitTestBase.GoUnitTestBase):
    directory = "al2/go/event-bridge-schema"
    code_directories = ["hello-world"]

class UnitTest_provided_go_cookiecutter_aws_sam_hello_step_functions_sample_app(UnitTestBase.GoUnitTestBase):
    directory = "al2/go/step-func"
    code_directories = ["functions/stockBuyer", "functions/stockChecker", "functions/stockSeller"]

class UnitTest_provided_go_cookiecutter_aws_sam_response_streaming_sample_app(UnitTestBase.GoUnitTestBase):
    directory = "al2/go/response-streaming"
    code_directories = ["hello"]
