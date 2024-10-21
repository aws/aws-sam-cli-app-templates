from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_nodejs22_x_cookiecutter_aws_sam_hello_nodejs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/hello"
    code_directories = ["hello-world"]
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/step-func"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_quick_start_from_scratch(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/scratch"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_quick_start_cloudwatch_events(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/cw-event"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_quick_start_response_streaming(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/response-streaming"
    code_directories = ["src"]
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_quick_start_s3(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/s3"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_quick_start_sns(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/sns"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_quick_start_sqs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/sqs"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_quick_start_web(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/web"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_quick_start_full_stack(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/full-stack"
    code_directories = ["backend", "frontend"]
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class UnitTest_nodejs22_x_cookiecutter_aws_sam_gql_quick_start(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs22.x/hello-gql"
    code_directories = ["greeter"]
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False
