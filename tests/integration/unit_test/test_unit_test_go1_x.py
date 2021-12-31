from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_go1_x_cookiecutter_aws_sam_hello_golang(UnitTestBase.GoUnitTestBase):
    directory = "go1.x/cookiecutter-aws-sam-hello-golang"
    code_directories = ["hello-world"]


class UnitTest_go1_x_cookiecutter_aws_sam_hello_step_functions_sample_app(UnitTestBase.GoUnitTestBase):
    directory = "go1.x/cookiecutter-aws-sam-hello-step-functions-sample-app"
    code_directories = ["functions/stockBuyer", "functions/stockChecker", "functions/stockSeller"]
