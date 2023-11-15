from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_nodejs20_x_cookiecutter_aws_sam_hello_nodejs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/hello"
    code_directories = ["hello-world"]
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/step-func"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_from_scratch(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/scratch"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_cloudwatch_events(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/cw-event"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_response_streaming(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/response-streaming"
    code_directories = ["src"]
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_s3(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/s3"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_sns(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/sns"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_sqs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/sqs"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_web(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/web"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_quick_start_full_stack(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/full-stack"
    code_directories = ["backend", "frontend"]
    # TODO (hawflau): remove after GA
    should_test_lint = False


class UnitTest_nodejs20_x_cookiecutter_aws_sam_gql_quick_start(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs20.x/hello-gql"
    code_directories = ["greeter"]
    should_test_lint = False
