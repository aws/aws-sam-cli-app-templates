from unittest import skip

from tests.integration.base import Base


class UnitTest_java11_cookiecutter_aws_sam_hello_java_gradle(Base.JavaUnitTestGradleBase):
    directory = "java11/cookiecutter-aws-sam-hello-java-gradle"
    code_directories = ["HelloWorldFunction"]


class UnitTest_java11_cookiecutter_aws_sam_hello_java_maven(Base.JavaUnitTestMavenBase):
    directory = "java11/cookiecutter-aws-sam-hello-java-maven"
    code_directories = ["HelloWorldFunction"]


class UnitTest_java11_cookiecutter_aws_sam_eventbridge_hello_java_gradle(Base.JavaUnitTestGradleBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-hello-java-gradle"
    code_directories = ["HelloWorldFunction"]


class UnitTest_java11_cookiecutter_aws_sam_eventbridge_hello_java_maven(Base.JavaUnitTestMavenBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-hello-java-maven"
    code_directories = ["HelloWorldFunction"]


@skip("eventbridge schema app requires credential to pull missing files, skip")
class UnitTest_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(Base.JavaUnitTestGradleBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-schema-app-java-gradle"
    code_directories = ["HelloWorldFunction"]


@skip("eventbridge schema app requires credential to pull missing files, skip")
class UnitTest_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(Base.JavaUnitTestMavenBase):
    directory = "java11/cookiecutter-aws-sam-eventbridge-schema-app-java-maven"
    code_directories = ["HelloWorldFunction"]


class UnitTest_java11_cookiecutter_aws_sam_step_functions_sample_app_gradle(Base.JavaUnitTestGradleBase):
    directory = "java11/cookiecutter-aws-sam-step-functions-sample-app-gradle"
    code_directories = [
        "functions/StockBuyer",
        "functions/StockChecker",
        "functions/StockSeller",
    ]


class UnitTest_java11_cookiecutter_aws_sam_step_functions_sample_app_maven(Base.JavaUnitTestMavenBase):
    directory = "java11/cookiecutter-aws-sam-step-functions-sample-app-maven"
    code_directories = [
        "functions/StockBuyer",
        "functions/StockChecker",
        "functions/StockSeller",
    ]
