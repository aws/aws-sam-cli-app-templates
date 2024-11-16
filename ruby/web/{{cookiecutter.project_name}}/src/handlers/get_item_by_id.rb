# frozen_string_literal: true

require "aws-sdk-dynamodb"

class ItemNotFoundError < StandardError; end

def handler(event:, context:)
  id = event["pathParameters"]["id"]

  data = client.get_item(
    table_name: ENV["SAMPLE_TABLE"],
    key: { "id" => id }
  )
  item = data.item

  raise ItemNotFoundError if item.nil?

  { statusCode: 200, body: item.to_json }
rescue ItemNotFoundError
  { statusCode: 404, body: { error: "Item #{id} not found" }.to_json }
end

def client
  @client ||= Aws::DynamoDB::Client.new
end
