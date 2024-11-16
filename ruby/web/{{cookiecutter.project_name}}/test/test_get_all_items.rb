# frozen_string_literal: true

require "minitest/autorun"
require_relative "../src/handlers/get_all_items"

class TestGetAllItems < Minitest::Test
  def setup
    ENV["SAMPLE_TABLE"] = "test_table"
    @client = Aws::DynamoDB::Client.new(stub_responses: true)
  end

  def test_get_all_items
    @client.stub_responses(:scan, {
                             items: [
                               { "id" => "123", "name" => "Test Item" },
                               { "id" => "456", "name" => "Test Item 2" }
                             ]
                           })

    response = handler(event: {}, context: nil)

    assert_equal 200, response[:statusCode]
    assert_equal(
      [
        { "id" => "123", "name" => "Test Item" },
        { "id" => "456", "name" => "Test Item 2" }
      ].to_json, response[:body]
    )
  end
end
