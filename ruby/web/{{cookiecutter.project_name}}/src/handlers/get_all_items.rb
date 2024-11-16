# frozen_string_literal: true

require "aws-sdk-dynamodb"

def handler(event:, context:)
  data = client.scan(table_name: ENV["SAMPLE_TABLE"])
  items = data.items

  { statusCode: 200, body: items.to_json }
end

def client
  @client ||= Aws::DynamoDB::Client.new
end
