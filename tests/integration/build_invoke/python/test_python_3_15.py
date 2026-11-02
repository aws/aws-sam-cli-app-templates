from unittest import skip
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_python3_15_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.15/hello"
    should_test_lint: bool = False


class BuildInvoke_python3_15_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.15/event-bridge"
    should_test_lint: bool = False


class BuildInvoke_python3_15_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "python3.15/web-conn"
    should_test_lint: bool = False


class BuildInvoke_python3_15_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.15/step-func-conn"
    should_test_lint: bool = False


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_15_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.15/event-bridge-schema"
    should_test_lint: bool = False


class BuildInvoke_python3_15_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.15/step-func"
    should_test_lint: bool = False


# if we want to check response json, we need to setup efs
class BuildInvoke_python3_15_cookiecutter_aws_sam_efs_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.15/efs"
    should_test_lint: bool = False


class BuildInvoke_python3_15_cookiecutter_aws_sam_hello_pt_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.15/hello-pt"
    should_test_lint: bool = False


class BuildInvoke_image_python3_15_cookiecutter_aws_sam_hello_python_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "python3.15/hello-img"
    should_test_lint: bool = False

# TODO: uncomment below and add the template back in manifest-v2.json once PyTorch supports python3.15
# class BuildInvoke_python3_15_pytorch(BuildInvokeBase.BuildInvokeBase):
#     directory = "python3.15/apigw-pytorch"

class BuildInvoke_python3_15_scikit(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.15/apigw-scikit"
    should_test_lint: bool = False

# TODO: uncomment below and add the template back in manifest-v2.json once Tensorflow supports python3.15
# class BuildInvoke_python3_15_tensorflow(BuildInvokeBase.BuildInvokeBase):
#     directory = "python3.15/apigw-tensorflow"

class BuildInvoke_python3_15_xgboost(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.15/apigw-xgboost"
    should_test_lint: bool = False
