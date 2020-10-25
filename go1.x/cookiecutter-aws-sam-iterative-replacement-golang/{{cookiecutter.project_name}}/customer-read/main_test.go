package main

import (
	"testing"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-sdk-go/service/dynamodb"
	"github.com/aws/aws-sdk-go/service/dynamodb/dynamodbiface"
)

type mockedGetItem struct {
	dynamodbiface.DynamoDBAPI
	Response dynamodb.GetItemOutput
}

func (d mockedGetItem) GetItem(in *dynamodb.GetItemInput) (*dynamodb.GetItemOutput, error) {
	return &d.Response, nil
}

func TestLambdaHandler(t *testing.T) {
	t.Run("Successful Request", func(t *testing.T) {

		m := mockedGetItem{
			Response: dynamodb.GetItemOutput{},
		}

		d := dependency{
			ddb:   m,
			table: "test_table",
		}

		_, err := d.LambdaHandler(events.APIGatewayProxyRequest{})
		if err != nil {
			t.Fatal("Everything should be ok")
		}
	})
}
