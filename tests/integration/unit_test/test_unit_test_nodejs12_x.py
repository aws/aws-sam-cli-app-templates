from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_nodejs12_x_cookiecutter_aws_sam_hello_nodejs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-aws-sam-hello-nodejs"
    code_directories = ["hello-world"]


class UnitTest_nodejs12_x_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-aws-sam-step-functions-sample-app"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]


class UnitTest_nodejs12_x_cookiecutter_quick_start_from_scratch(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-from-scratch"


class UnitTest_nodejs12_x_cookiecutter_quick_start_cloudwatch_events(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-cloudwatch-events"


class UnitTest_nodejs12_x_cookiecutter_quick_start_s3(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-s3"


class UnitTest_nodejs12_x_cookiecutter_quick_start_sns(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-sns"


class UnitTest_nodejs12_x_cookiecutter_quick_start_sqs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-sqs"


class UnitTest_nodejs12_x_cookiecutter_quick_start_web(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-web"

class UnitTest_nodejs12_x_cookiecutter_typescript_app_template(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-typescript-app-template"
    code_directories = [ "app" ]