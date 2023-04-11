from unittest import skip
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_python3_7_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.7/hello"


class BuildInvoke_python3_7_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.7/event-bridge"


class BuildInvoke_python3_7_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "python3.7/web-conn"


class BuildInvoke_python3_7_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.7/step-func-conn"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_7_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.7/event-bridge-schema"


class BuildInvoke_python3_7_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.7/step-func"

class BuildInvoke_image_python3_7_cookiecutter_aws_sam_hello_python_lambda_image(
    (BuildInvokeBase.SimpleHelloWorldBuildInvokeBase)
):
    directory = "python3.7/hello-img"

class BuildInvoke_python3_7_cookiecutter_aws_sam_hello_pt_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.7/hello-pt"
