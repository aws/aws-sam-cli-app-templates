from random import randint


def lambda_handler(event, context):
    """Sample Lambda function which mocks the operation of checking the current price 
    of a stock.

    For demonstration purposes this Lambda function simply returns 
    a random integer between 0 and 100 as the stock price.

    Parameters
    ----------
    event: dict, required
        Input event to the Lambda function

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
        dict: Object containing the current price of the stock
    """
    # Check current price of the stock
    stock_price = randint(
        0, 100
    )  # Current stock price is mocked as a random integer between 0 and 100
    return {"stock_price": stock_price}
