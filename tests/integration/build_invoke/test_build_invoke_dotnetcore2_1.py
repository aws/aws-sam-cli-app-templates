from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
sam build does not support to build dotnetcore 2.1 templates using container, 
here we put them in a separate file and use a dedicate codebuild project with .net 2.1 runtime to build them.

For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""


class BuildInvoke_dotnetcore2_1_cookiecutter_aws_sam_hello_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnetcore2.1/cookiecutter-aws-sam-hello-dotnet"


class BuildInvoke_dotnetcore2_1_cookiecutter_aws_sam_hello_step_functions_sample_app(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnetcore2.1/cookiecutter-aws-sam-hello-step-functions-sample-app"


#
# Image templates
#


class BuildInvoke_image_dotnetcore2_1_cookiecutter_aws_sam_hello_dotnet_lambda_image(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    directory = "dotnetcore2.1-image/cookiecutter-aws-sam-hello-dotnet-lambda-image"
