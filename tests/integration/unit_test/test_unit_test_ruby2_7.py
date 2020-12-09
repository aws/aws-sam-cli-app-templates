from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_ruby2_7_cookiecutter_aws_sam_hello_ruby(UnitTestBase.RubyUnitTestBase):
    directory = "ruby2.7/cookiecutter-aws-sam-hello-ruby"
    code_directories = ["tests/unit/test_handler.rb"]


class UnitTest_ruby2_7_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.RubyUnitTestBase):
    directory = "ruby2.7/cookiecutter-aws-sam-step-functions-sample-app"
    code_directories = [
        "tests/unit/test_stock_buyer.rb",
        "tests/unit/test_stock_checker.rb",
        "tests/unit/test_stock_seller.rb",
    ]
