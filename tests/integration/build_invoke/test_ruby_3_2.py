from unittest import skip
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_ruby3_2_cookiecutter_aws_sam_hello_ruby(BuildInvokeBase.HelloWorldExclamationBuildInvokeBase):
    directory = "ruby3.2/hello"
    # TODO: Remove this line when Ruby3.2 is GA.
    should_test_lint = False


class BuildInvoke_ruby3_2_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "ruby3.2/step-func"
    # TODO: Remove this line when Ruby3.2 is GA.
    should_test_lint = False

class BuildInvoke_image_ruby3_2_cookiecutter_aws_sam_hello_ruby_lambda_image(
    BuildInvokeBase.HelloWorldExclamationBuildInvokeBase
):
    directory = "ruby3.2/hello-img"
