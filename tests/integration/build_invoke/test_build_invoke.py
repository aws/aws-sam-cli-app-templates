from unittest import skip
from tests.integration.base import Base


class BuildInvoke_java8_cookiecutter_aws_sam_hello_java_gradle(Base.HelloWorldWithLocationBuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-hello-java-gradle"


class BuildInvoke_java8_cookiecutter_aws_sam_hello_java_maven(Base.HelloWorldWithLocationBuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-hello-java-maven"


class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_hello_java_gradle(Base.EventBridgeHelloWorldBuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-eventbridge-hello-java-gradle"


class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_hello_java_maven(Base.EventBridgeHelloWorldBuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-eventbridge-hello-java-maven"


@skip("eventbridge schema app seems not be able to build")
class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(Base.BuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-eventbridge-schema-app-java-gradle"


@skip("eventbridge schema app seems not be able to build")
class BuildInvoke_java8_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(Base.BuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-eventbridge-schema-app-java-maven"


class BuildInvoke_java8_cookiecutter_aws_sam_step_functions_sample_app_gradle(Base.BuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-step-functions-sample-app-gradle"


class BuildInvoke_java8_cookiecutter_aws_sam_step_functions_sample_app_maven(Base.BuildInvokeBase):
    directory = "java8/cookiecutter-aws-sam-step-functions-sample-app-maven"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_hello_java_gradle(Base.HelloWorldWithLocationBuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-hello-java-gradle"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_hello_java_maven(Base.HelloWorldWithLocationBuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-hello-java-maven"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_hello_java_gradle(
    Base.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8.al2/cookiecutter-aws-sam-eventbridge-hello-java-gradle"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_hello_java_maven(
    Base.EventBridgeHelloWorldBuildInvokeBase
):
    directory = "java8.al2/cookiecutter-aws-sam-eventbridge-hello-java-maven"


@skip("eventbridge schema app seems not be able to build")
class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(Base.BuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-eventbridge-schema-app-java-gradle"


@skip("eventbridge schema app seems not be able to build")
class BuildInvoke_java8_al2_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(Base.BuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-eventbridge-schema-app-java-maven"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_step_functions_sample_app_gradle(Base.BuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-hello-java-step-functions-sample-app-gradle"


class BuildInvoke_java8_al2_cookiecutter_aws_sam_step_functions_sample_app_maven(Base.BuildInvokeBase):
    directory = "java8.al2/cookiecutter-aws-sam-hello-java-step-functions-sample-app-maven"


class BuildInvoke_java11_cookiecutter_aws_sam_hello_java_gradle(Base.HelloWorldWithLocationBuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-hello-java-gradle"


class BuildInvoke_java11_cookiecutter_aws_sam_hello_java_maven(Base.HelloWorldWithLocationBuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-hello-java-maven"


class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_hello_java_gradle(Base.EventBridgeHelloWorldBuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-hello-java-gradle"


class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_hello_java_maven(Base.EventBridgeHelloWorldBuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-hello-java-maven"


@skip("eventbridge schema app seems not be able to build")
class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(Base.BuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-schema-app-java-gradle"


@skip("eventbridge schema app seems not be able to build")
class BuildInvoke_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(Base.BuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-schema-app-java-maven"


class BuildInvoke_java11_cookiecutter_aws_sam_step_functions_sample_app_gradle(Base.BuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-step-functions-sample-app-gradle"


class BuildInvoke_java11_cookiecutter_aws_sam_step_functions_sample_app_maven(Base.BuildInvokeBase):
    directory = "java11/cookiecutter-aws-sam-step-functions-sample-app-maven"


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_hello_nodejs(Base.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-aws-sam-hello-nodejs"


class BuildInvoke_nodejs12_x_cookiecutter_aws_sam_step_functions_sample_app(Base.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_from_scratch(Base.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-from-scratch"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_cloudwatch_events(Base.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-cloudwatch-events"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_s3(Base.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-s3"

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sns(Base.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-sns"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_sqs(Base.BuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-sqs"


class BuildInvoke_nodejs12_x_cookiecutter_quick_start_web(Base.QuickStartWebBuildInvokeBase):
    directory = "nodejs12.x/cookiecutter-quick-start-web"

    # if we want to check response json, we need to setup dynamodb


class BuildInvoke_nodejs10_x_cookiecutter_aws_sam_hello_nodejs(Base.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs10.x/cookiecutter-aws-sam-hello-nodejs"


class BuildInvoke_nodejs10_x_cookiecutter_quick_start_from_scratch(Base.BuildInvokeBase):
    directory = "nodejs10.x/cookiecutter-quick-start-from-scratch"


class BuildInvoke_nodejs10_x_cookiecutter_quick_start_cloudwatch_events(Base.BuildInvokeBase):
    directory = "nodejs10.x/cookiecutter-quick-start-cloudwatch-events"


class BuildInvoke_nodejs10_x_cookiecutter_quick_start_s3(Base.BuildInvokeBase):
    directory = "nodejs10.x/cookiecutter-quick-start-s3"

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs10_x_cookiecutter_quick_start_sns(Base.BuildInvokeBase):
    directory = "nodejs10.x/cookiecutter-quick-start-sns"


class BuildInvoke_nodejs10_x_cookiecutter_quick_start_sqs(Base.BuildInvokeBase):
    directory = "nodejs10.x/cookiecutter-quick-start-sqs"


class BuildInvoke_nodejs10_x_cookiecutter_quick_start_web(Base.QuickStartWebBuildInvokeBase):
    directory = "nodejs10.x/cookiecutter-quick-start-web"

    # if we want to check response json, we need to setup dynamodb


class BuildInvoke_nodejs10_x_cookiecutter_aws_sam_step_functions_sample_app(Base.BuildInvokeBase):
    directory = "nodejs10.x/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_python2_7_cookiecutter_aws_sam_hello_python(Base.SimpleHelloWorldBuildInvokeBase):
    directory = "python2.7/cookiecutter-aws-sam-hello-python"


class BuildInvoke_python2_7_cookiecutter_aws_sam_step_functions_sample_app(Base.BuildInvokeBase):
    directory = "python2.7/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_python3_6_cookiecutter_aws_sam_hello_python(Base.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.6/cookiecutter-aws-sam-hello-python"


class BuildInvoke_python3_6_cookiecutter_aws_sam_eventBridge_python(Base.EventBridgeHelloWorldBuildInvokeBase):
    directory = "python3.6/cookiecutter-aws-sam-eventBridge-python"


@skip("eventbridge schema app seems not be able to build")
class BuildInvoke_python3_6_cookiecutter_aws_sam_eventbridge_schema_app_python(Base.BuildInvokeBase):
    directory = "python3.6/cookiecutter-aws-sam-eventbridge-schema-app-python"


class BuildInvoke_python3_6_cookiecutter_aws_sam_step_functions_sample_app(Base.BuildInvokeBase):
    directory = "python3.6/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_python3_7_cookiecutter_aws_sam_hello_python(Base.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.7/cookiecutter-aws-sam-hello-python"


class BuildInvoke_python3_7_cookiecutter_aws_sam_eventBridge_python(Base.EventBridgeHelloWorldBuildInvokeBase):
    directory = "python3.7/cookiecutter-aws-sam-eventBridge-python"


@skip("eventbridge schema app seems not be able to build")
class BuildInvoke_python3_7_cookiecutter_aws_sam_eventbridge_schema_app_python(Base.BuildInvokeBase):
    directory = "python3.7/cookiecutter-aws-sam-eventbridge-schema-app-python"


class BuildInvoke_python3_7_cookiecutter_aws_sam_step_functions_sample_app(Base.BuildInvokeBase):
    directory = "python3.7/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_python3_8_cookiecutter_aws_sam_hello_python(Base.SimpleHelloWorldBuildInvokeBase):
    directory = "python3.8/cookiecutter-aws-sam-hello-python"


class BuildInvoke_python3_8_cookiecutter_aws_sam_eventBridge_python(Base.EventBridgeHelloWorldBuildInvokeBase):
    directory = "python3.8/cookiecutter-aws-sam-eventBridge-python"


@skip("eventbridge schema app seems not be able to build")
class BuildInvoke_python3_8_cookiecutter_aws_sam_eventbridge_schema_app_python(Base.BuildInvokeBase):
    directory = "python3.8/cookiecutter-aws-sam-eventbridge-schema-app-python"


class BuildInvoke_python3_8_cookiecutter_aws_sam_step_functions_sample_app(Base.BuildInvokeBase):
    directory = "python3.8/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_python3_8_cookiecutter_aws_sam_efs_python(Base.BuildInvokeBase):
    directory = "python3.8/cookiecutter-aws-sam-efs-python"

    # if we want to check response json, we need to setup efs


class BuildInvoke_ruby2_5_cookiecutter_aws_sam_hello_ruby(Base.HelloWorldExclamationBuildInvokeBase):
    directory = "ruby2.5/cookiecutter-aws-sam-hello-ruby"


class BuildInvoke_ruby2_5_cookiecutter_aws_sam_step_functions_sample_app(Base.BuildInvokeBase):
    directory = "ruby2.5/cookiecutter-aws-sam-step-functions-sample-app"


class BuildInvoke_ruby2_7_cookiecutter_aws_sam_hello_ruby(Base.HelloWorldExclamationBuildInvokeBase):
    directory = "ruby2.7/cookiecutter-aws-sam-hello-ruby"


class BuildInvoke_ruby2_7_cookiecutter_aws_sam_step_functions_sample_app(Base.BuildInvokeBase):
    directory = "ruby2.7/cookiecutter-aws-sam-step-functions-sample-app"
