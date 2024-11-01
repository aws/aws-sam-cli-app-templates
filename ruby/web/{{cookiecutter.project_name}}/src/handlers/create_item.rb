# frozen_string_literal: true

require "aws-sdk-dynamodb"

class ItemAlreadyExistsError < StandardError; end

def handler(event:, context:)
  body = JSON.parse(event["body"])
  item = body.slice("id", "name")

  existing_item = client.get_item(
    table_name: ENV["SAMPLE_TABLE"],
    key: { "id" => item["id"] }
  ).item

  raise ItemAlreadyExistsError unless existing_item.nil?

  client.put_item(
    table_name: ENV["SAMPLE_TABLE"],
    item: item
  )

  { statusCode: 201, body: item.to_json }
rescue ItemAlreadyExistsError
  { statusCode: 409, body: { error: "Item #{item['id']} already exists" }.to_json }
end

def client
  @client ||= Aws::DynamoDB::Client.new
end
