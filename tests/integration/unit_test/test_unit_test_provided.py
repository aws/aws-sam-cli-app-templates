from tests.integration.unit_test.unit_test_base import UnitTestBase

class UnitTest_provided_cookiecutter_aws_sam_hello_rustlang(UnitTestBase.RustUnitTestBase):
    directory = "rust/cookiecutter-aws-sam-hello-rust"
    code_directories = ["hello-world"]
