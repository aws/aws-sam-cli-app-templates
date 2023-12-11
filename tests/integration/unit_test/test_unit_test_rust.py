from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_rust_cookiecutter_aws_sam_hello_rust(UnitTestBase.RustUnitTestBase):
    directory = "al2/rust/hello"

class UnitTest_rust_al2023_cookiecutter_aws_sam_hello_rust(UnitTestBase.RustUnitTestBase):
    directory = "al2023/rust/hello"
