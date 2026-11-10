from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_nodejs26_x_cookiecutter_aws_sam_hello_nodejs(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/hello"
    code_directories = ["hello-world"]
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/step-func"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_quick_start_from_scratch(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/scratch"
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_quick_start_cloudwatch_events(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/cw-event"
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_quick_start_response_streaming(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/response-streaming"
    code_directories = ["src"]
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_quick_start_s3(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/s3"
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_quick_start_sns(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/sns"
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_quick_start_sqs(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/sqs"
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_quick_start_web(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/web"
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_quick_start_full_stack(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/full-stack"
    code_directories = ["backend", "frontend"]
    # It can be removed after SAM CLI consumes cfn-lint that adds support for nodejs26.x
    should_test_lint = False


class UnitTest_nodejs26_x_cookiecutter_aws_sam_gql_quick_start(UnitTestBase.NodejsUnitTestBase):
    runtime = "nodejs26.x"
    directory = "nodejs/hello-gql"
    code_directories = ["greeter"]
    should_test_lint = False
