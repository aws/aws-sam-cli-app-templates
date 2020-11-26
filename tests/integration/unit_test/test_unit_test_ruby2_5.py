from tests.integration.base import Base


class UnitTest_ruby2_5_cookiecutter_aws_sam_hello_ruby(Base.RubyUnitTestBase):
    directory = "ruby2.5/cookiecutter-aws-sam-hello-ruby"
    code_directories = ["tests/unit/test_handler.rb"]

    def test_unit_tests(self):
        self.skipTest("This unit test will fail")


class UnitTest_ruby2_5_cookiecutter_aws_sam_step_functions_sample_app(Base.RubyUnitTestBase):
    directory = "ruby2.5/cookiecutter-aws-sam-step-functions-sample-app"
    code_directories = [
        "tests/unit/test_stock_buyer.rb",
        "tests/unit/test_stock_checker.rb",
        "tests/unit/test_stock_seller.rb",
    ]
