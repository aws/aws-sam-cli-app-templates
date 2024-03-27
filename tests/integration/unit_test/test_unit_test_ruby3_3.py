from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_ruby3_3_cookiecutter_aws_sam_hello_ruby(UnitTestBase.RubyUnitTestBase):
    runtime = "ruby3.3"
    directory = "ruby/hello"
    code_directories = ["tests/unit/test_handler.rb"]
    # TODO(hawflau): remove the line below when cfn-lint supports ruby3.3
    should_test_lint = False


class UnitTest_ruby3_3_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.RubyUnitTestBase):
    runtime = "ruby3.3"
    directory = "ruby/step-func"
    code_directories = [
        "tests/unit/test_stock_buyer.rb",
        "tests/unit/test_stock_checker.rb",
        "tests/unit/test_stock_seller.rb",
    ]
    # TODO(hawflau): remove the line below when cfn-lint supports ruby3.3
    should_test_lint = False
