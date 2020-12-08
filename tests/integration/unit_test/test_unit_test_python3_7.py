from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_python3_7_cookiecutter_aws_sam_hello_python(UnitTestBase.Python37UnitTestBase):
    directory = "python3.7/cookiecutter-aws-sam-hello-python"
    code_directories = ["hello_world"]


class UnitTest_python3_7_cookiecutter_aws_sam_eventBridge_python(UnitTestBase.Python37UnitTestBase):
    directory = "python3.7/cookiecutter-aws-sam-eventBridge-python"
    code_directories = ["hello_world_function"]


class UnitTest_python3_7_cookiecutter_aws_sam_eventbridge_schema_app_python(UnitTestBase.Python37UnitTestBase):
    directory = "python3.7/cookiecutter-aws-sam-eventbridge-schema-app-python"
    code_directories = ["hello_world_function"]

    def _test_unit_tests(self, code_directory: str):
        self.skipTest("eventbridge schema app requires credential to pull missing files, skip")
        pass


class UnitTest_python3_7_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.Python37UnitTestBase):
    directory = "python3.7/cookiecutter-aws-sam-step-functions-sample-app"
    code_directories = [
        "functions/stock_buyer",
        "functions/stock_checker",
        "functions/stock_seller",
    ]
