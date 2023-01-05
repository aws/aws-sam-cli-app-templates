from unittest import skip
from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""


class BuildInvoke_java8_cookiecutter_aws_sam_hello_java_gradle(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java8/hello-gradle"


class BuildInvoke_java8_cookiecutter_aws_sam_hello_java_maven(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java8/hello-maven"


class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_hello_java_gradle(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8/event-bridge-gradle"


class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_hello_java_maven(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8/event-bridge-maven"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java8/event-bridge-schema-gradle"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java8/event-bridge-schema-maven"


class BuildInvoke_java8_cookiecutter_aws_sam_step_functions_sample_app_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java8/step-func-gradle"


class BuildInvoke_java8_cookiecutter_aws_sam_step_functions_sample_app_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java8/step-func-maven"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_hello_java_gradle(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java8.al2/hello-gradle"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_hello_java_maven(
    BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase
):
    directory = "java8.al2/hello-maven"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_hello_java_gradle(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8.al2/event-bridge-gradle"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_hello_java_maven(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8.al2/event-bridge-maven"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java8.al2/event-bridge-schema-gradle"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java8.al2/event-bridge-schema-maven"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_step_functions_sample_app_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java8.al2/step-func-gradle"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_step_functions_sample_app_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java8.al2/step-func-maven"


class BuildInvoke_java11_cookiecutter_aws_sam_hello_java_gradle(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java11/hello-gradle"


class BuildInvoke_java11_cookiecutter_aws_sam_hello_java_maven(BuildInvokeBase.HelloWorldWithLocationBuildInvokeBase):
    directory = "java11/hello-maven"


class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_hello_java_gradle(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java11/event-bridge-gradle"


class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_hello_java_maven(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java11/event-bridge-maven"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java11/event-bridge-schema-gradle"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java11/event-bridge-schema-maven"


class BuildInvoke_java11_cookiecutter_aws_sam_step_functions_sample_app_gradle(BuildInvokeBase.BuildInvokeBase):
    directory = "java11/step-func-gradle"


class BuildInvoke_java11_cookiecutter_aws_sam_step_functions_sample_app_maven(BuildInvokeBase.BuildInvokeBase):
    directory = "java11/step-func-maven"


# class BuildInvoke_nodejs18_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
#     directory = "nodejs18.x/hello"


# class BuildInvoke_nodejs18_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
#     directory = "nodejs18.x/step-func"


# class BuildInvoke_nodejs18_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
#     directory = "nodejs18.x/scratch"


# class BuildInvoke_nodejs18_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
#     directory = "nodejs18.x/cw-event"


# class BuildInvoke_nodejs18_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
#     directory = "nodejs18.x/s3"

#     # if we want to check response json, we need to setup bucket for testing


# class BuildInvoke_nodejs18_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
#     directory = "nodejs18.x/sns"


# class BuildInvoke_nodejs18_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
#     directory = "nodejs18.x/sqs"


# class BuildInvoke_nodejs18_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
#     directory = "nodejs18.x/web"


class BuildInvoke_nodejs16_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs16.x/hello"


class BuildInvoke_nodejs16_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/step-func"


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/scratch"


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/cw-event"


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/s3"

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/sns"


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs16.x/sqs"


class BuildInvoke_nodejs16_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs16.x/web"

class BuildInvoke_nodejs14_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs14.x/hello"


class BuildInvoke_nodejs14_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/step-func"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/scratch"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/cw-event"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/s3"

    # if we want to check response json, we need to setup bucket for testing

class BuildInvoke_nodejs14_x_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs14.x/web-conn"


class BuildInvoke_nodejs14_x_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/step-func-conn"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/sns"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs14.x/sqs"


class BuildInvoke_nodejs14_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs14.x/web"


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs12.x/hello"


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/step-func"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/scratch"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/cw-event"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/s3"

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs12.x/web-conn"


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/step-func-conn"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/sns"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs12.x/sqs"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs12.x/web"


class BuildInvoke_python3_7_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.7/hello"


class BuildInvoke_python3_7_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.7/event-bridge"


class BuildInvoke_python3_7_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "python3.7/web-conn"


class BuildInvoke_python3_7_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.7/step-func-conn"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_7_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.7/event-bridge-schema"


class BuildInvoke_python3_7_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.7/step-func"


class BuildInvoke_python3_8_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.8/hello"


class BuildInvoke_python3_8_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.8/event-bridge"


class BuildInvoke_python3_8_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "python3.9/web-conn"


class BuildInvoke_python3_8_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.8/step-func-conn"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_8_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.8/event-bridge-schema"


class BuildInvoke_python3_8_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.8/step-func"


class BuildInvoke_python3_8_cookiecutter_aws_sam_efs_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.8/efs"


class BuildInvoke_python3_9_cookiecutter_aws_sam_hello_python(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.9/hello"


class BuildInvoke_python3_9_cookiecutter_aws_sam_eventBridge_python(
    BuildInvokeBase.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "python3.9/event-bridge"

class BuildInvoke_python3_9_cookiecutter_aws_sam_quick_start_web_with_connectors(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "python3.9/web-conn"


class BuildInvoke_python3_9_cookiecutter_aws_sam_step_functions_with_connectors(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.9/step-func-conn"


@skip("eventbridge schema app requires credential to pull missing files, skip")
class BuildInvoke_python3_9_cookiecutter_aws_sam_eventbridge_schema_app_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.9/event-bridge-schema"


class BuildInvoke_python3_9_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.9/step-func"


class BuildInvoke_python3_9_cookiecutter_aws_sam_efs_python(BuildInvokeBase.BuildInvokeBase):
    directory = "python3.9/efs"


# if we want to check response json, we need to setup efs


class BuildInvoke_ruby2_7_cookiecutter_aws_sam_hello_ruby(BuildInvokeBase.HelloWorldExclamationBuildInvokeBase):
    directory = "ruby2.7/hello"


class BuildInvoke_ruby2_7_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "ruby2.7/step-func"
