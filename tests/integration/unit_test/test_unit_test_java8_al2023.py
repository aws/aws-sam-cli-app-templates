from unittest import skip

from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_java8_al2023_cookiecutter_aws_sam_hello_java_gradle(UnitTestBase.JavaUnitTestGradleBase):
    directory = "java8.al2023/hello-gradle"
    should_test_lint = False
    code_directories = ["HelloWorldFunction"]


class UnitTest_java8_al2023_cookiecutter_aws_sam_hello_img_java_gradle(UnitTestBase.JavaUnitTestGradleBase):
    directory = "java8.al2023/hello-img-gradle"
    should_test_lint = False
    code_directories = ["HelloWorldFunction"]


class UnitTest_java8_al2023_cookiecutter_aws_sam_hello_img_java_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java8.al2023/hello-img-maven"
    should_test_lint = False
    code_directories = ["HelloWorldFunction"]


class UnitTest_java8_al2023_cookiecutter_aws_sam_hello_java_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java8.al2023/hello-maven"
    should_test_lint = False
    code_directories = ["HelloWorldFunction"]


class UnitTest_java8_al2023_cookiecutter_aws_sam_hello_java_powertools_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java8.al2023/hello-pt-maven"
    should_test_lint = False
    code_directories = ["HelloWorldFunction"]


class UnitTest_java8_al2023_cookiecutter_aws_sam_eventbridge_hello_java_gradle(UnitTestBase.JavaUnitTestGradleBase):
    directory = "java8.al2023/event-bridge-gradle"
    should_test_lint = False
    code_directories = ["HelloWorldFunction"]


class UnitTest_java8_al2023_cookiecutter_aws_sam_eventbridge_hello_java_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java8.al2023/event-bridge-maven"
    should_test_lint = False
    code_directories = ["HelloWorldFunction"]


@skip("eventbridge schema app requires credential to pull missing files, skip")
class UnitTest_java8_al2023_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(UnitTestBase.JavaUnitTestGradleBase):
    directory = "java8.al2023/event-bridge-schema-gradle"
    should_test_lint = False
    code_directories = ["HelloWorldFunction"]


@skip("eventbridge schema app requires credential to pull missing files, skip")
class UnitTest_java8_al2023_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java8.al2023/event-bridge-schema-maven"
    should_test_lint = False
    code_directories = ["HelloWorldFunction"]


class UnitTest_java8_al2023_cookiecutter_aws_sam_step_functions_sample_app_gradle(UnitTestBase.JavaUnitTestGradleBase):
    directory = "java8.al2023/step-func-gradle"
    should_test_lint = False
    code_directories = [
        "functions/StockBuyer",
        "functions/StockChecker",
        "functions/StockSeller",
    ]


class UnitTest_java8_al2023_cookiecutter_aws_sam_step_functions_sample_app_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java8.al2023/step-func-maven"
    should_test_lint = False
    code_directories = [
        "functions/StockBuyer",
        "functions/StockChecker",
        "functions/StockSeller",
    ]
