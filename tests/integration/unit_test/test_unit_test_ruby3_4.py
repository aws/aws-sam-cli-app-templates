from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_ruby3_4_cookiecutter_aws_sam_hello_ruby(UnitTestBase.RubyUnitTestBase):
    runtime = "ruby3.4"
    directory = "ruby/hello"
    code_directories = ["tests/unit/test_handler.rb"]
    # It can be removed after cfn-lint supports ruby3.4
    should_test_lint = False


class UnitTest_ruby3_4_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.RubyUnitTestBase):
    runtime = "ruby3.4"
    directory = "ruby/step-func"
    should_test_lint = False
    code_directories = [
        "tests/unit/test_stock_buyer.rb",
        "tests/unit/test_stock_checker.rb",
        "tests/unit/test_stock_seller.rb",
    ]

class UnitTest_ruby3_4_cookiecutter_quick_start_web(UnitTestBase.RubyUnitTestBase):
    runtime = "ruby3.4"
    directory = "ruby/web"
    should_test_lint = False
    code_directories = [
        "test/test_create_item.rb",
        "test/test_delete_item.rb",
        "test/test_get_all_items.rb",
        "test/test_get_item_by_id.rb",
        "test/test_update_item.rb"
    ]
