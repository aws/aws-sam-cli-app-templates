import pytest

from tests.integration.base import Base

# sam build is likely to fail in the first try because dotnet.lambda cannot be used immediately after installation
# rerun can make it work


@pytest.mark.flaky(reruns=2)
class BuildInvoke_dotnetcore2_1_cookiecutter_aws_sam_hello_dotnet(Base.BuildInvokeBase):
    use_container = False
    directory = "dotnetcore2.1/cookiecutter-aws-sam-hello-dotnet"


@pytest.mark.flaky(reruns=2)
class BuildInvoke_dotnetcore2_1_cookiecutter_aws_sam_hello_step_functions_sample_app(Base.BuildInvokeBase):
    use_container = False
    directory = "dotnetcore2.1/cookiecutter-aws-sam-hello-step-functions-sample-app"


#
# Image templates
#


class BuildInvoke_image_dotnetcore2_1_cookiecutter_aws_sam_hello_dotnet_lambda_image:
    directory = "dotnetcore2.1-image/cookiecutter-aws-sam-hello-dotnet-lambda-image"
