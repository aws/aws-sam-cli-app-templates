from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
sam build does not support to build dotnetcore 3.1 templates using container, 
here we put them in a separate file and use a dedicate codebuild project with .net 3.1 runtime to build them.

For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_graalvm_java11_cookiecutter_aws_sam_graalvm_gradle(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "graalvm/java11/cookiecutter-aws-sam-graalvm-gradle"
    build_image_tag = "al2-graalvm-java11"


class BuildInvoke_graalvm_java11_cookiecutter_aws_sam_graalvm_maven(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "graalvm/java11/cookiecutter-aws-sam-graalvm-maven"
    build_image_tag = "al2-graalvm-java11"


class BuildInvoke_graalvm_java17_cookiecutter_aws_sam_graalvm_gradle(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "graalvm/java17/cookiecutter-aws-sam-graalvm-gradle"
    build_image_tag = "al2-graalvm-java17"


class BuildInvoke_graalvm_java17_cookiecutter_aws_sam_graalvm_maven(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "graalvm/java17/cookiecutter-aws-sam-graalvm-maven"
    build_image_tag = "al2-graalvm-java17"

