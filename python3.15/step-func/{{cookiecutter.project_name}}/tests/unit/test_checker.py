from functions.stock_checker import app


def test_stock_checker():
    data = app.lambda_handler(None, "")
    assert 0 <= data["stock_price"] > 0 <= 100
