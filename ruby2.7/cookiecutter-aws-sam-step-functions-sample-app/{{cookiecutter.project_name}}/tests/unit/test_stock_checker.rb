require 'test/unit'

require_relative '../../functions/stock_checker/app'

class StockCheckerTest < Test::Unit::TestCase
  def test_lambda_handler
    result = lambda_handler(event: nil, context: '')
    assert_true(result.key?("stock_price"))
    stock_price = result['stock_price']
    assert_true(stock_price.between?(0, 100))
  end
end
