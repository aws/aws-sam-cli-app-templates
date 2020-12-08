from tests.integration.base import Base

# dotnet unit tests are executed from test directories, so code_directories point to test directories


class UnitTest_dotnetcore2_1_cookiecutter_aws_sam_hello_dotnet(Base.DotNetCoreUnitTestBase):
    directory = "dotnetcore2.1/cookiecutter-aws-sam-hello-dotnet"
    code_directories = ["test/HelloWorld.Test"]


class UnitTest_dotnetcore2_1_cookiecutter_aws_sam_hello_step_functions_sample_app(Base.DotNetCoreUnitTestBase):
    directory = "dotnetcore2.1/cookiecutter-aws-sam-hello-step-functions-sample-app"
    code_directories = ["tests/StockBuyer.Test", "tests/StockChecker.Test", "tests/StockSeller.Test"]
