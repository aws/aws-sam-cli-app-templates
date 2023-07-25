
import pytest
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_java17_cookiecutter_aws_sam_hello_java_gradle(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java17/hello-gradle"


class BuildInvoke_java17_cookiecutter_aws_sam_hello_java_maven(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java17/hello-maven"


class BuildInvoke_java17_cookiecutter_aws_sam_eventbridge_hello_java_gradle(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java17/event-bridge-gradle"


class BuildInvoke_java17_cookiecutter_aws_sam_eventbridge_hello_java_maven(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java17/event-bridge-maven"


@pytest.mark.skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java17_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java17/event-bridge-schema-gradle"


@pytest.mark.skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java17_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java17/event-bridge-schema-maven"


class BuildInvoke_java17_cookiecutter_aws_sam_powertools_hello_app_java_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java17/hello-pt-gradle"


class BuildInvoke_java17_cookiecutter_aws_sam_powertools_hello_app_java_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java17/hello-pt-maven"


class BuildInvoke_java17_cookiecutter_aws_sam_step_functions_sample_app_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java17/step-func-gradle"


class BuildInvoke_java17_cookiecutter_aws_sam_step_functions_sample_app_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java17/step-func-maven"


class BuildInvoke_image_java17_cookiecutter_aws_sam_hello_java_gradle_lambda_image(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java17/hello-img-gradle"


class BuildInvoke_image_java17_cookiecutter_aws_sam_hello_java_maven_lambda_image(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java17/hello-img-maven"
