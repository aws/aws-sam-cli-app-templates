from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
sam build does not support to build dotnetcore 3.1 templates using container, 
here we put them in a separate file and use a dedicate codebuild project with .net 3.1 runtime to build them.

For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""


class BuildInvoke_dotnet6_cookiecutter_aws_sam_hello_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet6/hello"
    should_test_lint: bool = False


class BuildInvoke_dotnet6_cookiecutter_aws_sam_hello_dotnet_pt(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet6/hello-pt"
    should_test_lint: bool = False


# FIXME: fix and re-enable the test
# class BuildInvoke_dotnet6_cookiecutter_aws_sam_hello_powershell(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
#     use_container = False
#     directory = "dotnet6/hello-ps"


class BuildInvoke_dotnet6_cookiecutter_aws_sam_quick_start_s3_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet6/s3"
    should_test_lint: bool = False


class BuildInvoke_dotnet6_cookiecutter_aws_sam_quick_start_sns_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet6/sns"
    should_test_lint: bool = False


class BuildInvoke_dotnet6_cookiecutter_aws_sam_quick_start_sqs_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet6/sqs"
    should_test_lint: bool = False


class BuildInvoke_dotnet6_cookiecutter_aws_sam_hello_step_functions_sample_app(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet6/step-func"
    should_test_lint: bool = False


class BuildInvoke_dotnet6_cookiecutter_aws_sam_quick_start_cloudwatch_events_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet6/cw-event"
    should_test_lint: bool = False


class BuildInvoke_dotnet6_cookiecutter_aws_from_scratch_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet6/scratch"
    should_test_lint: bool = False


class BuildInvoke_dotnet6_cookiecutter_aws_sam_quick_start_web_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet6/web"
    should_test_lint: bool = False


#
# Image templates
#


class BuildInvoke_image_dotnet6_cookiecutter_aws_sam_hello_dotnet_lambda_image(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    directory = "dotnet6/hello-img"
    should_test_lint: bool = False
