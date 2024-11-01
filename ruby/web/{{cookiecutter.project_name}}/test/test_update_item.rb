# frozen_string_literal: true

require "minitest/autorun"
require_relative "../src/handlers/update_item"

class TestUpdateItem < Minitest::Test
  def setup
    ENV["SAMPLE_TABLE"] = "test_table"
    @client = Aws::DynamoDB::Client.new(stub_responses: true)
  end

  def test_update_item_success
    event = { "pathParameters" => { "id" => "123" }, "body" => { "name" => "Updated Item" }.to_json }

    @client.stub_responses(:get_item, { item: { "id" => "123" } })
    @client.stub_responses(:update_item, { attributes: { "id" => "123", "name" => "Updated Item" } })

    response = handler(event: event, context: nil)

    assert_equal 200, response[:statusCode]
    assert_equal({ "id" => "123", "name" => "Updated Item" }.to_json, response[:body])
  end

  def test_update_item_not_found
    event = { "pathParameters" => { "id" => "123" }, "body" => { "name" => "Updated Item" }.to_json }

    @client.stub_responses(:get_item, { item: nil })

    response = handler(event: event, context: nil)

    assert_equal 404, response[:statusCode]
    assert_includes response[:body], "not found"
  end
end
