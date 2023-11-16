from unittest import skip
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_python3_12_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.12/hello"
    should_test_lint: bool = False


class BuildInvoke_python3_12_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.12/event-bridge"
    should_test_lint: bool = False

class BuildInvoke_python3_12_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "python3.12/web-conn"
    should_test_lint: bool = False


class BuildInvoke_python3_12_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.12/step-func-conn"
    should_test_lint: bool = False


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_12_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.12/event-bridge-schema"
    should_test_lint: bool = False


class BuildInvoke_python3_12_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.12/step-func"
    should_test_lint: bool = False


# if we want to check response json, we need to setup efs
class BuildInvoke_python3_12_cookiecutter_aws_sam_efs_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.12/efs"
    should_test_lint: bool = False


class BuildInvoke_python3_12_cookiecutter_aws_sam_hello_pt_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.12/hello-pt"
    should_test_lint: bool = False


class BuildInvoke_image_python3_12_cookiecutter_aws_sam_hello_python_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "python3.12/hello-img"
    should_test_lint: bool = False

# TODO: uncomment below and add the template back in manifest-v2.json once PyTorch supports Python3.12
# class BuildInvoke_python3_12_pytorch(BuildInvokeBase.BuildInvokeBase):
#     directory = "python3.12/apigw-pytorch"
#     should_test_lint: bool = False

class BuildInvoke_python3_12_scikit(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.12/apigw-scikit"
    should_test_lint: bool = False

# TODO: uncomment below and add the template back in manifest-v2.json once Tensorflow supports Python3.12
# class BuildInvoke_python3_12_tensorflow(BuildInvokeBase.BuildInvokeBase):
#     directory = "python3.12/apigw-tensorflow"
#     should_test_lint: bool = False

class BuildInvoke_python3_12_xgboost(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.12/apigw-xgboost"
    should_test_lint: bool = False
