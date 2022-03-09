# dotnet unit tests are executed from test directories, so code_directories point to test directories
from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_dotnet6_cookiecutter_aws_sam_hello_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/cookiecutter-aws-sam-hello-dotnet"
    code_directories = ["test/HelloWorld.Test"]


# FIXME: fix and re-enable the test
# class UnitTest_dotnet6_cookiecutter_aws_sam_hello_powershell(UnitTestBase.DotNetCoreUnitTestBase):
#     directory = "dotnet6/cookiecutter-aws-sam-hello-powershell"
#     code_directories = ["test/HelloWorld.Test"]


class UnitTest_dotnet6_cookiecutter_aws_sam_hello_step_functions_sample_app(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/cookiecutter-aws-sam-hello-step-functions-sample-app"
    code_directories = ["tests/StockBuyer.Test", "tests/StockChecker.Test", "tests/StockSeller.Test"]


class UnitTest_dotnet6_cookiecutter_aws_sam_cloudwatch_events_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/cookiecutter-aws-sam-quick-start-cloudwatch-events-dotnet"
    code_directories = ["test/project.Tests"]
class UnitTest_dotnet6_cookiecutter_aws_sam_quickstart_sns_dotnet_sample_app(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/cookiecutter-aws-sam-quickstart-sns-dotnet"
    code_directories = ["test/project.Tests"]

class UnitTest_dotnet6_cookiecutter_aws_from_scratch_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/cookiecutter-aws-sam-quick-start-from-scratch-dotnet"
    code_directories = ["test/project.Tests"]

    
class UnitTest_dotnet6_cookiecutter_aws_sam_quick_start_web_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/cookiecutter-aws-sam-quick-start-web-dotnet"
    code_directories = ["tests/project.Tests"]


class UnitTest_dotnet6_cookiecutter_aws_sam_quick_start_sqs(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/cookiecutter-aws-sam-quick-start-sqs-dotnet"
    code_directories = ["test/project.Tests"]
