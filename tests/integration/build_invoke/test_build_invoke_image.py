from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""


class BuildInvoke_image_nodejs14_x_cookiecutter_aws_sam_hello_nodejs_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "nodejs14.x-image/cookiecutter-aws-sam-hello-nodejs-lambda-image"


class BuildInvoke_image_nodejs12_x_cookiecutter_aws_sam_hello_nodejs_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "nodejs12.x-image/cookiecutter-aws-sam-hello-nodejs-lambda-image"


class BuildInvoke_image_python3_9_cookiecutter_aws_sam_hello_python_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "python3.9-image/cookiecutter-aws-sam-hello-python-lambda-image"


class BuildInvoke_image_python3_8_cookiecutter_aws_sam_hello_python_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "python3.8-image/cookiecutter-aws-sam-hello-python-lambda-image"


class BuildInvoke_image_ruby2_7_cookiecutter_aws_sam_hello_ruby_lambda_image(
    BuildInvokeBase.HelloWorldExclamationBuildInvokeBase
):
    directory = "ruby2.7-image/cookiecutter-aws-sam-hello-ruby-lambda-image"


class BuildInvoke_image_java11_cookiecutter_aws_sam_hello_java_gradle_lambda_image(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java11-image/cookiecutter-aws-sam-hello-java-gradle-lambda-image"


class BuildInvoke_image_java11_cookiecutter_aws_sam_hello_java_maven_lambda_image(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java11-image/cookiecutter-aws-sam-hello-java-maven-lambda-image"


class BuildInvoke_image_python3_7_cookiecutter_aws_sam_hello_python_lambda_image(
    (BuildInvokeBase.SimpleHelloWorldBuildInvokeBase)
):
    directory = "python3.7-image/cookiecutter-aws-sam-hello-python-lambda-image"


class BuildInvoke_image_python3_6_cookiecutter_aws_sam_hello_python_lambda_image(
    (BuildInvokeBase.SimpleHelloWorldBuildInvokeBase)
):
    directory = "python3.6-image/cookiecutter-aws-sam-hello-python-lambda-image"


class BuildInvoke_image_java8_cookiecutter_aws_sam_hello_java_gradle_lambda_image(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java8-image/cookiecutter-aws-sam-hello-java-gradle-lambda-image"


class BuildInvoke_image_java8_cookiecutter_aws_sam_hello_java_maven_lambda_image(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java8-image/cookiecutter-aws-sam-hello-java-maven-lambda-image"


class BuildInvoke_image_java8_al2_cookiecutter_aws_sam_hello_java_gradle_lambda_image(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java8.al2-image/cookiecutter-aws-sam-hello-java-gradle-lambda-image"


class BuildInvoke_image_java8_al2_cookiecutter_aws_sam_hello_java_maven_lambda_image(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java8.al2-image/cookiecutter-aws-sam-hello-java-maven-lambda-image"
