package main

import (
	"encoding/json"
	"os"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"
	"github.com/aws/aws-sdk-go/service/dynamodb/dynamodbattribute"
	"github.com/aws/aws-sdk-go/service/dynamodb/dynamodbiface"
	"github.com/segmentio/ksuid"
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
			table: os.Getenv("DYNAMODB_TABLE"),
		}
	}

	// Create a new record from the request
	r := Record{
		ID:   ksuid.New().String(),
		Body: request.Body,
	}

	// Marshal that record into a DynamoDB AttributeMap
	av, err := dynamodbattribute.MarshalMap(r)
	if err != nil {
		return events.APIGatewayProxyResponse{}, err
	}

	// Save the AttributeMap in the given table
	_, err = d.ddb.PutItem(&dynamodb.PutItemInput{
		TableName: aws.String(d.table),
		Item:      av,
	})

	if err != nil {
		return events.APIGatewayProxyResponse{}, err
	}

	body, err := json.Marshal(r)
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
