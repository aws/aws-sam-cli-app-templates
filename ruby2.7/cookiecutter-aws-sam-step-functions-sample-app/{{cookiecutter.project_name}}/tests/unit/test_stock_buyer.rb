require 'test/unit'

require_relative '../../functions/stock_buyer/app'

class StockBuyerTest < Test::Unit::TestCase
  def test_lambda_handler
    stock_price = 75
    input_payload = {
      'stock_price' => stock_price
    }
    result = lambda_handler(event: input_payload, context: '')
    assert_true(result.key?(:id))
    assert_true(result.key?(:timestamp))
    assert_true(result.key?(:qty))

    assert_equal("buy", result[:type])
    assert_equal(stock_price.to_s, result[:price])
  end
end
