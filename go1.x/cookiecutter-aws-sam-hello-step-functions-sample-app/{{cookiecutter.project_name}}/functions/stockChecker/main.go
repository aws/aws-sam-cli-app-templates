package main

import (
    "context"
    "math/rand"
    "github.com/aws/aws-lambda-go/lambda"
)

type StockEvent struct {
	StockPrice int `json:"stockPrice"`
}

func handler(ctx context.Context) (StockEvent, error) {
	// Sample Lambda function which mocks the operation of checking the current price
    // of a stock.

    // For demonstration purposes this Lambda function simply returns
    // a random integer between 0 and 100 as the stock price.

    // Parameters
    // ----------
    // event: StockEvent, required
    //     Input event to the Lambda function

    // Returns
    // ------
    //     StockEvent: Object containing the current price of the stock

    // Check current price of the stock
    return StockEvent{StockPrice: rand.Intn(100)}, nil // Current stock price is mocked as a random integer from 0 to 99
}

func main() {
    rand.Seed(11)

	lambda.Start(handler)
}
