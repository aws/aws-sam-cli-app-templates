# dotnet unit tests are executed from test directories, so code_directories point to test directories
from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_dotnet6_cookiecutter_aws_sam_hello_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/hello"
    code_directories = ["test/HelloWorld.Test"]

class UnitTest_dotnet6_cookiecutter_aws_sam_hello_dotnet_pt(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/hello-pt"
    code_directories = ["test/HelloWorld.Test"]

# FIXME: fix and re-enable the test
# class UnitTest_dotnet6_cookiecutter_aws_sam_hello_powershell(UnitTestBase.DotNetCoreUnitTestBase):
#     directory = "dotnet6/hello-ps"
#     code_directories = ["test/HelloWorld.Test"]


class UnitTest_dotnet6_cookiecutter_aws_sam_hello_step_functions_sample_app(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/step-func"
    code_directories = ["tests/StockBuyer.Test", "tests/StockChecker.Test", "tests/StockSeller.Test"]


class UnitTest_dotnet6_cookiecutter_aws_sam_cloudwatch_events_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/cw-event"
    code_directories = ["test/project.Tests"]
class UnitTest_dotnet6_cookiecutter_aws_sam_quickstart_sns_dotnet_sample_app(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/sns"
    code_directories = ["test/project.Tests"]

class UnitTest_dotnet6_cookiecutter_aws_from_scratch_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/scratch"
    code_directories = ["test/project.Tests"]

class UnitTest_dotnet6_cookiecutter_aws_sam_quick_start_web_dotnet(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/web"
    code_directories = ["tests/project.Tests"]


class UnitTest_dotnet6_cookiecutter_aws_sam_quick_start_sqs(UnitTestBase.DotNetCoreUnitTestBase):
    directory = "dotnet6/sqs"
    code_directories = ["test/project.Tests"]
