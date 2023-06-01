from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_ruby3_2_cookiecutter_aws_sam_hello_ruby(UnitTestBase.RubyUnitTestBase):
    directory = "ruby3.2/hello"
    code_directories = ["tests/unit/test_handler.rb"]
    # TODO: Remove this line when Ruby3.2 is GA.
    should_test_lint = False


class UnitTest_ruby3_2_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.RubyUnitTestBase):
    directory = "ruby3.2/step-func"
    code_directories = [
        "tests/unit/test_stock_buyer.rb",
        "tests/unit/test_stock_checker.rb",
        "tests/unit/test_stock_seller.rb",
    ]
    # TODO: Remove this line when Ruby3.2 is GA.
    should_test_lint = False
