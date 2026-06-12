from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_nodejs20_x_cookiecutter_aws_sam_hello_nodejs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/hello"
    code_directories = ["hello-world"]
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/step-func"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_from_scratch(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/scratch"
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_cloudwatch_events(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/cw-event"
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_response_streaming(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/response-streaming"
    code_directories = ["src"]
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_s3(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/s3"
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_sns(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/sns"
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_sqs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/sqs"
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_web(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/web"
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_full_stack(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/full-stack"
    code_directories = ["backend", "frontend"]
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_aws_sam_gql_quick_start(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/hello-gql"
    code_directories = ["greeter"]
    should_test_lint = False
