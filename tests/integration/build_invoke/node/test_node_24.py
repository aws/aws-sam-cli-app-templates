from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_nodejs24_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/hello"

class BuildInvoke_nodejs24_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/step-func"


class BuildInvoke_nodejs24_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/scratch"


class BuildInvoke_nodejs24_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/cw-event"


class BuildInvoke_nodejs24_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/s3"


class BuildInvoke_nodejs24_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/sns"


class BuildInvoke_nodejs24_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/sqs"


class BuildInvoke_nodejs24_x_cookiecutter_quick_start_response_streaming(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/response-streaming"


class BuildInvoke_nodejs24_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/web"


class BuildInvoke_nodejs24_x_cookiecutter_quick_start_full_stack(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/full-stack"


class BuildInvoke_image_nodejs24_x_cookiecutter_aws_sam_hello_nodejs_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    runtime = "nodejs24.x"
    directory = "nodejs/hello-img"


class BuildInvoke_nodejs24_x_cookiecutter_aws_sam_gql_quick_start(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs24.x"
    directory = "nodejs/hello-gql"
    should_test_lint = False
