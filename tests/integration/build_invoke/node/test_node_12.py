from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

# NOTE: skipping lint test for all nodejs12.x templates as the runtime is to be deprecated (Mar 31, 2023).
# See: https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html

class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs12.x/hello"
    should_test_lint = False


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/step-func"
    should_test_lint = False


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/scratch"
    should_test_lint = False


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/cw-event"
    should_test_lint = False


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/s3"
    should_test_lint = False

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs12.x/web-conn"
    should_test_lint = False


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/step-func-conn"
    should_test_lint = False


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/sns"
    should_test_lint = False


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/sqs"
    should_test_lint = False


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs12.x/web"
    should_test_lint = False

class BuildInvoke_image_nodejs12_x_cookiecutter_aws_sam_hello_nodejs_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "nodejs12.x/hello-img"
    should_test_lint = False