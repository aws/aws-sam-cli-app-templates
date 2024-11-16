# frozen_string_literal: true

require "minitest/autorun"
require_relative "../src/handlers/get_item_by_id"

class TestGetItemById < Minitest::Test
  def setup
    ENV["SAMPLE_TABLE"] = "test_table"
    @client = Aws::DynamoDB::Client.new(stub_responses: true)
  end

  def test_get_item_by_id_success
    event = { "pathParameters" => { "id" => "123" } }

    @client.stub_responses(:get_item, { item: { "id" => "123", "name" => "Test Item" } })

    response = handler(event: event, context: nil)

    assert_equal 200, response[:statusCode]
    assert_equal({ "id" => "123", "name" => "Test Item" }.to_json, response[:body])
  end

  def test_get_item_by_id_not_found
    event = { "pathParameters" => { "id" => "123" } }

    @client.stub_responses(:get_item, { item: nil })

    response = handler(event: event, context: nil)

    assert_equal 404, response[:statusCode]
    assert_includes response[:body], "not found"
  end
end
