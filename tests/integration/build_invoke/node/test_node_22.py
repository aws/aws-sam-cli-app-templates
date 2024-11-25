from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_nodejs22_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs22.x/hello"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False

class BuildInvoke_nodejs22_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs22.x/step-func"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_nodejs22_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs22.x/scratch"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_nodejs22_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs22.x/cw-event"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_nodejs22_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs22.x/s3"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_nodejs22_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs22.x/sns"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_nodejs22_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs22.x/sqs"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_nodejs22_x_cookiecutter_quick_start_response_streaming(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs22.x/response-streaming"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_nodejs22_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs22.x/web"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_nodejs22_x_cookiecutter_quick_start_full_stack(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs22.x/full-stack"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_image_nodejs22_x_cookiecutter_aws_sam_hello_nodejs_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "nodejs22.x/hello-img"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False


class BuildInvoke_nodejs22_x_cookiecutter_aws_sam_gql_quick_start(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs22.x/hello-gql"
    # TODO: remove the line remove once nodejs22.x is GA
    should_test_lint = False
