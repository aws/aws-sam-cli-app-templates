from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_ruby3_3_cookiecutter_aws_sam_hello_ruby(UnitTestBase.RubyUnitTestBase):
    runtime = "ruby3.3"
    directory = "ruby/hello"
    code_directories = ["tests/unit/test_handler.rb"]


class UnitTest_ruby3_3_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.RubyUnitTestBase):
    runtime = "ruby3.3"
    directory = "ruby/step-func"
    code_directories = [
        "tests/unit/test_stock_buyer.rb",
        "tests/unit/test_stock_checker.rb",
        "tests/unit/test_stock_seller.rb",
    ]

class UnitTest_ruby3_3_cookiecutter_quick_start_web(UnitTestBase.RubyUnitTestBase):
    runtime = "ruby3.3"
    directory = "ruby/web"
    code_directories = [
        "test/test_create_item.rb",
        "test/test_delete_item.rb",
        "test/test_get_all_items.rb",
        "test/test_get_item_by_id.rb",
        "test/test_update_item.rb"
    ]
