const crypto = require("crypto");

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max)) + 1;
}

/**
 * Sample Lambda function which mocks the operation of buying a random number of shares for a stock.
 * For demonstration purposes, this Lambda function does not actually perform any  actual transactions. It simply returns a mocked result.
 * 
 * @param {Object} event - Input event to the Lambda function
 * @param {Object} context - Lambda Context runtime methods and attributes
 *
 * @returns {Object} object - Object containing details of the stock buying transaction
 * 
 */
exports.lambdaHandler = async (event, context) => {
    // Get the price of the stock provided as input
    stock_price = event["stock_price"]
    var date = new Date();
    // Mocked result of a stock buying transaction
    let transaction_result = {
        'id': crypto.randomBytes(16).toString("hex"), // Unique ID for the transaction
        'price': stock_price.toString(), // Price of each share
        'type': "buy", // Type of transaction(buy/ sell)
        'qty': getRandomInt(10).toString(),  // Number of shares bought / sold(We are mocking this as a random integer between 1 and 10)
        'timestamp': date.toISOString(),  // Timestamp of the when the transaction was completed
    }
    return transaction_result
};
