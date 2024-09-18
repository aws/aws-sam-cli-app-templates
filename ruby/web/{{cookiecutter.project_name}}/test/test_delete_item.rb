# frozen_string_literal: true

require "minitest/autorun"
require_relative "../src/handlers/delete_item"

class TestDeleteItem < Minitest::Test
  def setup
    ENV["SAMPLE_TABLE"] = "test_table"
    @client = Aws::DynamoDB::Client.new(stub_responses: true)
  end

  def test_delete_item_success
    event = { "pathParameters" => { "id" => "123" } }

    @client.stub_responses(:get_item, { item: { "id" => "123" } })
    @client.stub_responses(:delete_item, {})

    response = handler(event: event, context: nil)

    assert_equal 204, response[:statusCode]
  end

  def test_delete_item_not_found
    event = { "pathParameters" => { "id" => "123" } }

    @client.stub_responses(:get_item, { item: nil })

    response = handler(event: event, context: nil)

    assert_equal 404, response[:statusCode]
    assert_includes response[:body], "not found"
  end
end
