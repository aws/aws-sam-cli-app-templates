from tests.integration.unit_test.unit_test_base import UnitTestBase

# NOTE: skipping lint test for all nodejs12.x templates as the runtime is to be deprecated (Mar 31, 2023).
# See: https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html

class UnitTest_nodejs12_x_cookiecutter_aws_sam_hello_nodejs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/hello"
    code_directories = ["hello-world"]
    should_test_lint = False


class UnitTest_nodejs12_x_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/step-func"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]
    should_test_lint = False


class UnitTest_nodejs12_x_cookiecutter_quick_start_from_scratch(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/scratch"
    should_test_lint = False


class UnitTest_nodejs12_x_cookiecutter_quick_start_cloudwatch_events(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cw-event"
    should_test_lint = False


class UnitTest_nodejs12_x_cookiecutter_quick_start_s3(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/s3"
    should_test_lint = False


class UnitTest_nodejs12_x_cookiecutter_quick_start_sns(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/sns"
    should_test_lint = False


class UnitTest_nodejs12_x_cookiecutter_quick_start_sqs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/sqs"
    should_test_lint = False


class UnitTest_nodejs12_x_cookiecutter_quick_start_web(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/web"
    should_test_lint = False

class UnitTest_nodejs12_x_cookiecutter_typescript_app_template(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/ts"
    code_directories = [ "app" ]
    should_test_lint = False


class UnitTest_nodejs12_x_cookiecutter_aws_sam_quick_start_web_with_connectors(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/web-conn"
    should_test_lint = False

class UnitTest_nodejs12_x_cookiecutter_aws_sam_step_functions_with_connectors(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/step-func-conn"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]
    should_test_lint = False