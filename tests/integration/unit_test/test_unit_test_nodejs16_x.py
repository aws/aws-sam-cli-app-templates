from tests.integration.unit_test.unit_test_base import UnitTestBase

"""
Nodejs 16 is now deprecated and will fail the linter check. Skip running `sam validate --lint`
"""

class UnitTest_nodejs16_x_cookiecutter_aws_sam_hello_nodejs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/hello"
    code_directories = ["hello-world"]
    should_test_lint = False


class UnitTest_nodejs16_x_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/step-func"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]
    should_test_lint = False


class UnitTest_nodejs16_x_cookiecutter_quick_start_from_scratch(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/scratch"
    should_test_lint = False


class UnitTest_nodejs16_x_cookiecutter_quick_start_cloudwatch_events(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/cw-event"
    should_test_lint = False
    

class UnitTest_nodejs16_x_cookiecutter_quick_start_response_streaming(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/response-streaming"
    code_directories = ["src"]
    should_test_lint = False
    

class UnitTest_nodejs16_x_cookiecutter_quick_start_s3(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/s3"
    should_test_lint = False
    

class UnitTest_nodejs16_x_cookiecutter_quick_start_sns(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/sns"
    should_test_lint = False
    

class UnitTest_nodejs16_x_cookiecutter_quick_start_sqs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/sqs"
    should_test_lint = False
    

class UnitTest_nodejs16_x_cookiecutter_quick_start_web(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/web"
    should_test_lint = False
    

class UnitTest_nodejs16_x_cookiecutter_aws_sam_quick_start_web_with_connectors(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/web-conn"
    should_test_lint = False
    
    
class UnitTest_nodejs16_x_cookiecutter_aws_sam_step_functions_with_connectors(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs16.x/step-func-conn"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]
    should_test_lint = False
