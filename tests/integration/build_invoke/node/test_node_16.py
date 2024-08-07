from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json

Nodejs 16 is now deprecated and will fail the linter check. Skip running `sam validate --lint`
"""

class BuildInvoke_nodejs16_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs16.x/hello"
    should_test_lint = False
    

class BuildInvoke_nodejs16_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/step-func"
    should_test_lint = False
    

class BuildInvoke_nodejs16_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/scratch"
    should_test_lint = False
    

class BuildInvoke_nodejs16_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/cw-event"
    should_test_lint = False


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/s3"
    should_test_lint = False
    
    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/sns"
    should_test_lint = False


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/sqs"
    should_test_lint = False


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_response_streaming(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/response-streaming"
    should_test_lint = False


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs16.x/web"
    should_test_lint = False
    
class BuildInvoke_image_nodejs16_x_cookiecutter_aws_sam_hello_nodejs_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "nodejs16.x/hello-img"
    should_test_lint = False
