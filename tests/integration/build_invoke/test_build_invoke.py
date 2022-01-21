from unittest import skip
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""


class BuildInvoke_java8_cookiecutter_aws_sam_hello_java_gradle(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-hello-java-gradle"


class BuildInvoke_java8_cookiecutter_aws_sam_hello_java_maven(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-hello-java-maven"


class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_hello_java_gradle(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8/cookiecutter-aws-sam-eventbridge-hello-java-gradle"


class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_hello_java_maven(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8/cookiecutter-aws-sam-eventbridge-hello-java-maven"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-eventbridge-schema-app-java-gradle"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-eventbridge-schema-app-java-maven"


class BuildInvoke_java8_cookiecutter_aws_sam_step_functions_sample_app_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-step-functions-sample-app-gradle"


class BuildInvoke_java8_cookiecutter_aws_sam_step_functions_sample_app_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-step-functions-sample-app-maven"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_hello_java_gradle(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java8.al2/cookiecutter-aws-sam-hello-java-gradle"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_hello_java_maven(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java8.al2/cookiecutter-aws-sam-hello-java-maven"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_hello_java_gradle(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8.al2/cookiecutter-aws-sam-eventbridge-hello-java-gradle"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_hello_java_maven(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8.al2/cookiecutter-aws-sam-eventbridge-hello-java-maven"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-eventbridge-schema-app-java-gradle"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-eventbridge-schema-app-java-maven"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_step_functions_sample_app_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-step-functions-sample-app-gradle"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_step_functions_sample_app_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-step-functions-sample-app-maven"


class BuildInvoke_java11_cookiecutter_aws_sam_hello_java_gradle(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-hello-java-gradle"


class BuildInvoke_java11_cookiecutter_aws_sam_hello_java_maven(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-hello-java-maven"


class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_hello_java_gradle(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java11/cookiecutter-aws-sam-eventbridge-hello-java-gradle"


class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_hello_java_maven(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java11/cookiecutter-aws-sam-eventbridge-hello-java-maven"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-schema-app-java-gradle"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-schema-app-java-maven"


class BuildInvoke_java11_cookiecutter_aws_sam_step_functions_sample_app_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-step-functions-sample-app-gradle"


class BuildInvoke_java11_cookiecutter_aws_sam_step_functions_sample_app_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-step-functions-sample-app-maven"


class BuildInvoke_nodejs14_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs14.x/cookiecutter-aws-sam-hello-nodejs"


class BuildInvoke_nodejs14_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/cookiecutter-quick-start-from-scratch"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/cookiecutter-quick-start-cloudwatch-events"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/cookiecutter-quick-start-s3"

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/cookiecutter-quick-start-sns"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/cookiecutter-quick-start-sqs"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs14.x/cookiecutter-quick-start-web"


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-aws-sam-hello-nodejs"


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-from-scratch"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-cloudwatch-events"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-s3"

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-sns"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-sqs"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-web"


class BuildInvoke_python3_6_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.6/cookiecutter-aws-sam-hello-python"


class BuildInvoke_python3_6_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.6/cookiecutter-aws-sam-eventBridge-python"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_6_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.6/cookiecutter-aws-sam-eventbridge-schema-app-python"


class BuildInvoke_python3_6_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.6/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_python3_7_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.7/cookiecutter-aws-sam-hello-python"


class BuildInvoke_python3_7_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.7/cookiecutter-aws-sam-eventBridge-python"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_7_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.7/cookiecutter-aws-sam-eventbridge-schema-app-python"


class BuildInvoke_python3_7_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.7/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_python3_8_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.8/cookiecutter-aws-sam-hello-python"


class BuildInvoke_python3_8_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.8/cookiecutter-aws-sam-eventBridge-python"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_8_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.8/cookiecutter-aws-sam-eventbridge-schema-app-python"


class BuildInvoke_python3_8_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.8/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_python3_8_cookiecutter_aws_sam_efs_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.8/cookiecutter-aws-sam-efs-python"


class BuildInvoke_python3_9_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.9/cookiecutter-aws-sam-hello-python"


class BuildInvoke_python3_9_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.9/cookiecutter-aws-sam-eventBridge-python"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_9_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.9/cookiecutter-aws-sam-eventbridge-schema-app-python"


class BuildInvoke_python3_9_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.9/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_python3_9_cookiecutter_aws_sam_efs_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.9/cookiecutter-aws-sam-efs-python"


# if we want to check response json, we need to setup efs


class BuildInvoke_ruby2_7_cookiecutter_aws_sam_hello_ruby(BuildInvokeBase.HelloWorldExclamationBuildInvokeBase):
    directory = "ruby2.7/cookiecutter-aws-sam-hello-ruby"


class BuildInvoke_ruby2_7_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "ruby2.7/cookiecutter-aws-sam-step-functions-sample-app"
