import pytest

from tests.integration.base import Base


class BuildInvoke_dotnetcore2_1_cookiecutter_aws_sam_hello_dotnet(Base.BuildInvokeBase):
    use_container = False
    directory = "dotnetcore2.1/cookiecutter-aws-sam-hello-dotnet"


class BuildInvoke_dotnetcore2_1_cookiecutter_aws_sam_hello_step_functions_sample_app(Base.BuildInvokeBase):
    use_container = False
    directory = "dotnetcore2.1/cookiecutter-aws-sam-hello-step-functions-sample-app"


#
# Image templates
#


class BuildInvoke_image_dotnetcore2_1_cookiecutter_aws_sam_hello_dotnet_lambda_image:
    directory = "dotnetcore2.1-image/cookiecutter-aws-sam-hello-dotnet-lambda-image"
