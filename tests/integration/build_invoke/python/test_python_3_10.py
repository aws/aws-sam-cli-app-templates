from unittest import skip
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_python3_10_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.10/hello"
    # TODO: remove the line remove once python3.10 is GA
    should_test_lint = False


class BuildInvoke_python3_10_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.10/event-bridge"
    # TODO: remove the line remove once python3.10 is GA
    should_test_lint = False

class BuildInvoke_python3_10_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "python3.10/web-conn"
    # TODO: remove the line remove once python3.10 is GA
    should_test_lint = False


class BuildInvoke_python3_10_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.10/step-func-conn"
    # TODO: remove the line remove once python3.10 is GA
    should_test_lint = False


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_10_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.10/event-bridge-schema"
    # TODO: remove the line remove once python3.10 is GA
    should_test_lint = False


class BuildInvoke_python3_10_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.10/step-func"
    # TODO: remove the line remove once python3.10 is GA
    should_test_lint = False


# if we want to check response json, we need to setup efs
class BuildInvoke_python3_10_cookiecutter_aws_sam_efs_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.10/efs"
    # TODO: remove the line remove once python3.10 is GA
    should_test_lint = False


class BuildInvoke_python3_10_cookiecutter_aws_sam_hello_pt_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.10/hello-pt"
    # TODO: remove the line remove once python3.10 is GA
    should_test_lint = False


class BuildInvoke_image_python3_10_cookiecutter_aws_sam_hello_python_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "python3.10/hello-img"
    # TODO: remove the line remove once python3.10 is GA
    should_test_lint = False
