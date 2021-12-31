require 'json'
require 'securerandom'
require 'date'

def lambda_handler(event:, context:)
  # Sample Lambda function which mocks the operation of buying a random number
  # of shares for a stock.

  # For demonstration purposes, this Lambda function does not actually perform any 
  # actual transactions. It simply returns a mocked result.

  # Parameters
  # ----------
  # event: Hash, required
  #     Input event to the Lambda function

  # context: object, required
  #     Lambda Context runtime methods and attributes

  # Returns
  # ------
  #     dict: Object containing details of the stock buying transaction

  # Get the price of the stock provided as input
  stock_price = event["stock_price"]
  # Mocked result of a stock buying transaction
  {
      id: SecureRandom.uuid,  # Unique ID for the transaction
      price: stock_price.to_s,  # Price of each share
      type: "buy",  # Type of transaction (buy/sell)
      qty: rand(1...10).to_s,  # Number of shares bought/sold (We are mocking this as a random integer between 1 and 10)
      timestamp: DateTime.now.iso8601,  # Timestamp of the when the transaction was completed
  }
end
