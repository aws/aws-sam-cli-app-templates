from unittest import skip
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_ruby2_7_cookiecutter_aws_sam_hello_ruby(BuildInvokeBase.HelloWorldExclamationBuildInvokeBase):
    runtime = "ruby2.7"
    directory = "ruby/hello"


class BuildInvoke_ruby2_7_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    runtime = "ruby2.7"
    directory = "ruby/step-func"

class BuildInvoke_image_ruby2_7_cookiecutter_aws_sam_hello_ruby_lambda_image(
    BuildInvokeBase.HelloWorldExclamationBuildInvokeBase
):
    runtime = "ruby2.7"
    directory = "ruby/hello-img"
