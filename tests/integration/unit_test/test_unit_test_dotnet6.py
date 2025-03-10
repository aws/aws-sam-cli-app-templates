# dotnet unit tests are executed from test directories, so code_directories point to test directories
from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_dotnet6_cookiecutter_aws_sam_hello_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/hello"
    code_directories = ["test/HelloWorld.Test"]
    should_test_lint: bool = False

class UnitTest_dotnet6_cookiecutter_aws_sam_hello_dotnet_pt(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/hello-pt"
    code_directories = ["test/HelloWorld.Test"]
    should_test_lint: bool = False

# FIXME: fix and re-enable the test
# class UnitTest_dotnet6_cookiecutter_aws_sam_hello_powershell(UnitTestBase.DotNetCoreUnitTestBase):
#     directory = "dotnet6/hello-ps"
#     code_directories = ["test/HelloWorld.Test"]


class UnitTest_dotnet6_cookiecutter_aws_sam_hello_step_functions_sample_app(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/step-func"
    code_directories = ["tests/StockBuyer.Test", "tests/StockChecker.Test", "tests/StockSeller.Test"]
    should_test_lint: bool = False


class UnitTest_dotnet6_cookiecutter_aws_sam_quick_start_s3_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/s3"
    code_directories = ["test/S3EventSource.Tests"]
    should_test_lint: bool = False


class UnitTest_dotnet6_cookiecutter_aws_sam_cloudwatch_events_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/cw-event"
    code_directories = ["test/CloudWatchEventSource.Tests"]
    should_test_lint: bool = False


class UnitTest_dotnet6_cookiecutter_aws_sam_quickstart_sns_dotnet_sample_app(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/sns"
    code_directories = ["test/SNSEventSource.Tests"]
    should_test_lint: bool = False


class UnitTest_dotnet6_cookiecutter_aws_from_scratch_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/scratch"
    code_directories = ["test/ScratchLambda.Tests"]
    should_test_lint: bool = False


class UnitTest_dotnet6_cookiecutter_aws_sam_quick_start_web_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/web"
    code_directories = ["tests/ServerlessAPI.Tests"]
    should_test_lint: bool = False


class UnitTest_dotnet6_cookiecutter_aws_sam_quick_start_sqs(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/sqs"
    code_directories = ["test/SQSEventSource.Tests"]
    should_test_lint: bool = False
