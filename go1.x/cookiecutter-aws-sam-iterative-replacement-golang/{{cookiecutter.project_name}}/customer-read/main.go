package main

import (
	"encoding/json"
	"os"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"
	"github.com/aws/aws-sdk-go/service/dynamodb/dynamodbiface"
)

const (
	// DynamoDBTable is the name of the environment variable that provides the DynamoDB table name
	DynamoDBTable = "DYNAMODB_TABLE"
	// PathParameter is the URL path parameter in the request
	PathParameter = "id"
)

type dependency struct {
	// For dependency injection, you want to import {service}/{service}iface
	// and create members of type {service}iface/{Service}API
	// Examples:
	//   ddb    dynamodbiface.DynamoDBAPI
	//   s3svc  s3iface.S3API
	//   ssmsvc ssmiface.SSMAPI
	ddb   dynamodbiface.DynamoDBAPI
	table string
}

// Record represents one record in the DynamoDB table
type Record struct {
	ID   string `dynamodbav:"id"`
	Body string
}

func (d *dependency) LambdaHandler(request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	// Check for dependencies, e.g., test injections.
	// If not present, create them with a live session.
	//
	// NOTE: Performance is the same *or better* when initializing dependencies
	// inside the handler compared to inside main().
	// For testing, see https://rbsttr.tv/godi
	if d.ddb == nil {
		sess := session.Must(session.NewSession())
		svc := dynamodb.New(sess)

		d = &dependency{
			ddb:   svc,
			table: os.Getenv(DynamoDBTable),
		}
	}

	// Create a new GetItem request
	input := dynamodb.GetItemInput{
		Key: map[string]*dynamodb.AttributeValue{
			"id": {
				S: aws.String(request.PathParameters[PathParameter]),
			},
		},
		TableName: aws.String(d.table),
	}

	// Attempt to retrieve the item
	item, err := d.ddb.GetItem(&input)
	if err != nil {
		return events.APIGatewayProxyResponse{}, err
	}

	body, err := json.Marshal(item.Item)
	if err != nil {
		return events.APIGatewayProxyResponse{}, err
	}

	return events.APIGatewayProxyResponse{
		Body:       string(body),
		StatusCode: 200,
	}, nil
}

func main() {
	d := dependency{}

	lambda.Start(d.LambdaHandler)
}
