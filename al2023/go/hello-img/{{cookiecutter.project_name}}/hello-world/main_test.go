package main

import (
	"testing"

	"github.com/aws/aws-lambda-go/events"
)

func TestHandler(t *testing.T) {
	testCases := []struct {
		name          string
		request       events.APIGatewayProxyRequest
		expectedBody  string
		expectedError error
	}{
		{
			// mock a request with an empty SourceIP
			name: "empty IP",
			request: events.APIGatewayProxyRequest{
				RequestContext: events.APIGatewayProxyRequestContext{
					Identity: events.APIGatewayRequestIdentity{
						SourceIP: "",
					},
				},
			},
			expectedBody:  "Hello, world!\n",
			expectedError: nil,
		},
		{
			// mock a request with a localhost SourceIP
			name: "localhost IP",
			request: events.APIGatewayProxyRequest{
				RequestContext: events.APIGatewayProxyRequestContext{
					Identity: events.APIGatewayRequestIdentity{
						SourceIP: "127.0.0.1",
					},
				},
			},
			expectedBody:  "Hello, 127.0.0.1!\n",
			expectedError: nil,
		},
	}

	for _, testCase := range testCases {
		t.Run(testCase.name, func(t *testing.T) {
			response, err := handler(testCase.request)
			if err != testCase.expectedError {
				t.Errorf("Expected error %v, but got %v", testCase.expectedError, err)
			}

			if response.Body != testCase.expectedBody {
				t.Errorf("Expected response %v, but got %v", testCase.expectedBody, response.Body)
			}

			if response.StatusCode != 200 {
				t.Errorf("Expected status code 200, but got %v", response.StatusCode)
			}
		})
	}
}
