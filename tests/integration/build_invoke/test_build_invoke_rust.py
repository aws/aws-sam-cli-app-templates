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

class BuildInvoke_provided_rust_cookiecutter_aws_sam_hello(BuildInvokeBase.BuildInvokeBase):
    use_container = False
    directory = "al2/rust/hello"
    beta_features = True

class BuildInvoke_providedal2023_rust_cookiecutter_aws_sam_hello(BuildInvokeBase.BuildInvokeBase):
    use_container = False
    directory = "al2023/rust/hello"
    beta_features = True

class BuildInvoke_provided_rust_cookiecutter_aws_sam_hello_dynamodb(BuildInvokeBase.BuildInvokeBase):
    use_container = False
    directory = "al2/rust/hello-ddb"
    beta_features = True
