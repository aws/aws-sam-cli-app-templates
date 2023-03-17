package main

import (
	"context"
	"fmt"
	"github.com/aws/aws-lambda-go/lambda"
	"{{ cookiecutter.codegen_path }}"
)

/*
Description: This lambda handler reads an {{ cookiecutter.AWS_Schema_detail_type }} from the inputted AWSEvent, then
    updates the Detail Type (description of the type of AWS event).
Parameters:
- context: Object that provides information about the Lambda invocation, function, and execution environment.
- awsEvent: AWS EventBridge object that provides information such as the source, region, account the
    event is associated with.
Output: Stream ([]byte) of the updated AWSEvent after function logic completed.
*/
func handler(context context.Context, event {{ cookiecutter.codegen_package_name }}.AWSEvent) ([]byte , error) {
	// Retrieve {{ cookiecutter.AWS_Schema_name }} detail from event
	detail := event.Detail
	fmt.Println("Reading {{ cookiecutter.AWS_Schema_name }}: ", detail)

	// Developers write your event-driven business logic code here!
	// Make updates to the event payload
	fmt.Println("{{ cookiecutter.function_name }} updating event of " + event.DetailType)
	event.SetDetailType("{{ cookiecutter.function_name }} updated event of " + event.DetailType)

	// Return event as stream for further processing
	return {{ cookiecutter.codegen_package_name }}.Marshal(event)

}

func main() {
	lambda.Start(handler)
}
