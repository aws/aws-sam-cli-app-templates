function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

/**
 * Sample Lambda function which mocks the operation of checking the current price of a stock.
 * For demonstration purposes this Lambda function simply returns a random integer between 0 and 100 as the stock price.
 * 
 * @param {Object} event - Input event to the Lambda function
 * @param {Object} context - Lambda Context runtime methods and attributes
 *
 * @returns {Object} object - Object containing the current price of the stock
 * 
 */
export const lambdaHandler = async (event, context) => {
    // Check current price of the stock
    const stock_price = getRandomInt(100)  // Current stock price is mocked as a random integer between 0 and 100
    return { 'stock_price': stock_price }
};
