package main

import (
    "context"
    "math/rand"
    "strconv"
    "time"
    "github.com/aws/aws-lambda-go/lambda"
)

type StockEvent struct {
	StockPrice int `json:"stockPrice"`
}

type TransactionResult struct {
	Id string `json:"id"`
	Price string `json:"price"`
	TransactionType string `json:"transactionType"`
	Qty string `json:"qty"`
	Timestamp string `json:"timestamp"`
}

func handler(ctx context.Context, event StockEvent) (TransactionResult, error) {
	// Sample Lambda function which mocks the operation of buying a random number
    // of shares for a stock.

    // For demonstration purposes, this Lambda function does not actually perform any
    // actual transactions. It simply returns a mocked result.

    // Parameters
    // ----------
    // event: StockEvent, required
    //     Input event to the Lambda function

    // Returns
    // ------
    //     TransactionResult: Object containing details of the stock buying transaction

    // Get the price of the stock provided as input
    stockPrice := event.StockPrice

    // Mocked result of a stock buying transaction
    return TransactionResult{
        Id: strconv.FormatInt(rand.Int63n(1000), 10),  // Unique ID for the transaction
        Price: strconv.FormatInt(int64(stockPrice), 10),  // Price of each share
        TransactionType: "buy",  // Type of transaction (buy/sell)
        Qty: strconv.FormatInt((rand.Int63n(9) + 1), 10),  // Number of shares bought/sold (We are mocking this as a random integer between 1 and 10)
        Timestamp: time.Now().Format(time.RFC850),  // Timestamp of the when the transaction was completed
    }, nil
}

func main() {
    rand.Seed(11)

	lambda.Start(handler)
}
