from tests.integration.base import Base


class UnitTest_nodejs12_x_cookiecutter_aws_sam_hello_nodejs(Base.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-aws-sam-hello-nodejs"
    code_directories = ["hello-world"]


class UnitTest_nodejs12_x_cookiecutter_aws_sam_step_functions_sample_app(Base.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-aws-sam-step-functions-sample-app"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]


class UnitTest_nodejs12_x_cookiecutter_quick_start_from_scratch(Base.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-from-scratch"


class UnitTest_nodejs12_x_cookiecutter_quick_start_cloudwatch_events(Base.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-cloudwatch-events"


class UnitTest_nodejs12_x_cookiecutter_quick_start_s3(Base.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-s3"


class UnitTest_nodejs12_x_cookiecutter_quick_start_sns(Base.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-sns"


class UnitTest_nodejs12_x_cookiecutter_quick_start_sqs(Base.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-sqs"


class UnitTest_nodejs12_x_cookiecutter_quick_start_web(Base.NodejsUnitTestBase):
    directory = "nodejs12.x/cookiecutter-quick-start-web"
