from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
sam build does not support to build dotnetcore 3.1 templates using container, 
here we put them in a separate file and use a dedicate codebuild project with .net 3.1 runtime to build them.

For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""


class BuildInvoke_dotnet8_cookiecutter_aws_sam_hello_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet8/hello"


class BuildInvoke_dotnet8_cookiecutter_aws_sam_hello_dotnet_pt(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet8/hello-pt"


class BuildInvoke_dotnet8_cookiecutter_aws_sam_quick_start_s3_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet8/s3"


class BuildInvoke_dotnet8_cookiecutter_aws_sam_quick_start_sns_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet8/sns"


class BuildInvoke_dotnet8_cookiecutter_aws_sam_quick_start_sqs_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet8/sqs"


class BuildInvoke_dotnet8_cookiecutter_aws_sam_hello_step_functions_sample_app(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet8/step-func"


class BuildInvoke_dotnet8_cookiecutter_aws_sam_quick_start_cloudwatch_events_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet8/cw-event"


class BuildInvoke_dotnet8_cookiecutter_aws_from_scratch_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet8/scratch"


class BuildInvoke_dotnet8_cookiecutter_aws_sam_quick_start_web_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet8/web"


#
# Image templates
#


class BuildInvoke_image_dotnet8_cookiecutter_aws_sam_hello_dotnet_lambda_image(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    directory = "dotnet8/hello-img"
