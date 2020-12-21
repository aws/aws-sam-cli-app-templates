from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
sam build does not support to build dotnet 5.0 templates using container, 
here we put them in a separate file and use a dedicate codebuild project with .net 5.0 runtime to build them.

For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

#
# Image templates
#


class BuildInvoke_image_dotnet5_0_cookiecutter_aws_sam_hello_dotnet_lambda_image(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    directory = "dotnet5.0-image/cookiecutter-aws-sam-hello-dotnet-lambda-image"
