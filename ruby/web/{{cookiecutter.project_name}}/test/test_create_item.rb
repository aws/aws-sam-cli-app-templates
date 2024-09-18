# frozen_string_literal: true

require "minitest/autorun"
require_relative "../src/handlers/create_item"

class TestCreateItem < Minitest::Test
  def setup
    ENV["SAMPLE_TABLE"] = "test_table"
    @client = Aws::DynamoDB::Client.new(stub_responses: true)
  end

  def test_create_item_success
    event = { "body" => { "id" => "123", "name" => "Test Item" }.to_json }

    @client.stub_responses(:get_item, { item: nil })
    @client.stub_responses(:put_item, {})

    response = handler(event: event, context: nil)

    assert_equal 201, response[:statusCode]
    assert_equal({ "id" => "123", "name" => "Test Item" }.to_json, response[:body])
  end

  def test_create_item_already_exists
    event = { "body" => { "id" => "123", "name" => "Test Item" }.to_json }

    @client.stub_data(:get_item, { item: { "id" => "123" } })

    response = handler(event: event, context: nil)

    assert_equal 409, response[:statusCode]
    assert_includes response[:body], "already exists"
  end
end
