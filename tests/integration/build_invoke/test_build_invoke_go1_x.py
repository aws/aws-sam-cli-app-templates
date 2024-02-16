from unittest import skip
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
sam build does not support to build go 1.x templates using container, 
here we put them in a separate file and use a dedicate codebuild project with go 1.x runtime to build them.

For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""


class BuildInvoke_provided_go_cookiecutter_aws_sam_hello_golang(BuildInvokeBase.BuildInvokeBase):
    use_container = False
    directory = "al2/go/hello"

class BuildInvoke_providedal2023_go_cookiecutter_aws_sam_hello_golang(BuildInvokeBase.BuildInvokeBase):
    use_container = False
    directory = "al2023/go/hello"

class BuildInvoke_provided_go_cookiecutter_aws_sam_eventbridge_hello_golang(BuildInvokeBase.BuildInvokeBase):
    use_container = False
    directory = "al2/go/event-bridge"

class BuildInvoke_provided_go_cookiecutter_aws_sam_response_streaming_golang(BuildInvokeBase.BuildInvokeBase):
    use_container = False
    directory = "al2/go/response-streaming"

# todo: remove skip once tests are run in environment with AWS Credentials
@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_provided_go_cookiecutter_aws_sam_eventbridge_schema_app_golang(BuildInvokeBase.BuildInvokeBase):
    use_container = False
    directory = "al2/go/event-bridge-schema"

class BuildInvoke_provided_go_cookiecutter_aws_sam_hello_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    use_container = False
    directory = "al2/go/step-func"

#
# Image templates
#

class BuildInvoke_image_provided_go_cookiecutter_aws_sam_hello_golang_lambda_image(BuildInvokeBase.BuildInvokeBase):
    directory = "al2/go/hello-img"

class BuildInvoke_image_providedal2023_go_cookiecutter_aws_sam_hello_golang_lambda_image(BuildInvokeBase.BuildInvokeBase):
    directory = "al2023/go/hello-img"