from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs12.x/hello"


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/step-func"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/scratch"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/cw-event"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/s3"

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs12.x/web-conn"


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/step-func-conn"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/sns"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/sqs"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs12.x/web"
