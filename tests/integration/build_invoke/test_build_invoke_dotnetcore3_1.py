from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
sam build does not support to build dotnetcore 3.1 templates using container, 
here we put them in a separate file and use a dedicate codebuild project with .net 3.1 runtime to build them.

For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""


class BuildInvoke_dotnetcore3_1_cookiecutter_aws_sam_hello_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnetcore3.1/cookiecutter-aws-sam-hello-dotnet"


class BuildInvoke_dotnetcore3_1_cookiecutter_aws_sam_hello_step_functions_sample_app(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnetcore3.1/cookiecutter-aws-sam-hello-step-functions-sample-app"


class BuildInvoke_dotnetcore3_1_cookiecutter_aws_sam_quick_start_s3_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnetcore3.1/cookiecutter-aws-sam-quick-start-s3-dotnet"

    
class BuildInvoke_dotnetcore3_1_cookiecutter_aws_sam_quick_start_sqs_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnetcore3.1/cookiecutter-aws-sam-quick-start-sqs-dotnet"


class BuildInvoke_dotnetcore3_1_cookiecutter_aws_quickstart_sns_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnetcore3.1/cookiecutter-aws-sam-quick-start-sns-dotnet"

    
class BuildInvoke_dotnetcore3_1_cookiecutter_aws_from_scratch_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnetcore3.1/cookiecutter-aws-sam-quick-start-from-scratch-dotnet"

    
class BuildInvoke_dotnetcore3_1_cookiecutter_aws_sam_hello_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnetcore3.1/cookiecutter-aws-sam-quick-start-cloudwatch-events-dotnet"

    
class BuildInvoke_dotnetcore3_1_cookiecutter_aws_sam_quick_start_web_dotnet_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnetcore3.1/cookiecutter-aws-sam-quick-start-web-dotnet"


#
# Image templates
#


class BuildInvoke_image_dotnetcore3_1_cookiecutter_aws_sam_hello_dotnet_lambda_image(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    directory = "dotnetcore3.1-image/cookiecutter-aws-sam-hello-dotnet-lambda-image"
