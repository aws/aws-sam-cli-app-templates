from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_python3_13_cookiecutter_aws_sam_hello_python(UnitTestBase.Python313UnitTestBase):
    directory = "python3.13/hello"
    code_directories = ["hello_world"]
    # TODO: remove the line remove once python3.13 is GA
    should_test_lint = False


class UnitTest_python3_13_cookiecutter_aws_sam_eventBridge_python(UnitTestBase.Python313UnitTestBase):
    directory = "python3.13/event-bridge"
    code_directories = ["hello_world_function"]
    # TODO: remove the line remove once python3.13 is GA
    should_test_lint = False


class UnitTest_python3_13_cookiecutter_aws_sam_eventbridge_schema_app_python(UnitTestBase.Python313UnitTestBase):
    directory = "python3.13/event-bridge-schema"
    code_directories = ["hello_world_function"]
    # TODO: remove the line remove once python3.13 is GA
    should_test_lint = False

    def _test_unit_tests(self, code_directory: str):
        self.skipTest("eventbridge schema app requires credential to pull missing files, skip")
        pass


class UnitTest_python3_13_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.Python313UnitTestBase):
    directory = "python3.13/step-func"
    code_directories = [
        "functions/stock_buyer",
        "functions/stock_checker",
        "functions/stock_seller",
    ]
    # TODO: remove the line remove once python3.13 is GA
    should_test_lint = False


class UnitTest_python3_13_cookiecutter_aws_sam_efs_python(UnitTestBase.Python313UnitTestBase):
    directory = "python3.13/efs"
    code_directories = ["hello_efs"]
    # TODO: remove the line remove once python3.13 is GA
    should_test_lint = False


class UnitTest_python3_13_cookiecutter_aws_sam_quick_start_web_with_connectors(UnitTestBase.Python313UnitTestBase):
    directory = "python3.13/web-conn"
    code_directories = [
        "src/handlers/get_all_items", 
        "src/handlers/get_by_id", 
        "src/handlers/put_item"
    ]
    # TODO: remove the line remove once python3.13 is GA
    should_test_lint = False


class UnitTest_python3_13_cookiecutter_aws_sam_step_functions_with_connectors(UnitTestBase.Python313UnitTestBase):
    directory = "python3.13/step-func-conn"
    code_directories = [
        "functions/stock_buyer",
        "functions/stock_checker",
        "functions/stock_seller",
    ]
    # TODO: remove the line remove once python3.13 is GA
    should_test_lint = False


class UnitTest_python3_13_cookiecutter_aws_sam_hello_pt_python(UnitTestBase.Python313UnitTestBase):
    directory = "python3.13/hello-pt"
    code_directories = ["hello_world"]
    # TODO: remove the line remove once python3.13 is GA
    should_test_lint = False
