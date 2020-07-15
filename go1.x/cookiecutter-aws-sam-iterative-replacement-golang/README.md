# AWS SAM iterative replacement template for Go

This repository contains an AWS SAM iterative replacement template. Iterative replacement allows you to migrate a monolith one route at a time by placing an [Amazon API Gateway][api-gateway] [HTTP API][http-api] in front of your existing application. Once all traffic is proxied through your HTTP API, you rewrite routes one at a time to serverless components. This enables you to modernize your monolith while reducing risk.

This template takes a single parameter, `PassthroughTarget`, of the form _https://api.anycompany.com_. Note that there is no trailing forward slash at the end of the target.

This template produces a single output, `APIRoot`, which is the root URL of your new HTTP API.

This template also includes two routes and an [Amazon DynamoDB][dynamodb] table to get you started:

1. POST _/customer_ to create a new record
1. GET _/customer/{id}_ to retrieve a record

These routes are integrated with two separate [AWS Lambda][lambda] functions, _customer-read_ and _customer-write_. These functions execute with AWS SAM policy templates that appropriately restrict their access to the DynamoDB table.

## How to use this template

1. Install the [AWS SAM CLI][aws-sam-cli]
1. From a terminal, run `sam init`
1. Select option **2 - Custom Template Location**
1. Enter _gh:rts-rob/aws-sam-iterative-replacement-golang_
1. Provide a project name, e.g., _hello-world_
1. Change into the created directory
1. Build with `sam build`
1. Deploy with `sam deploy --guided`
    * You will need to provide your existing application root URL as the value for the `PassthroughTarget` parameter, e.g., _https://api.anycompany.com_. Do not include a forward slash `"/"` at the end.

Now you have a sample application with [Amazon API Gateway][api-gateway], [Amazon DynamoDB][dynamodb], and [AWS Lambda][lambda] deployed and running in the region you specified. Your HTTP API will forward all traffic to your `PassthroughTarget` **except for** the routes you explicitly define in your AWS SAM template.

## Next steps

Once deployed, implement your actual route logic one route and method at a time. Shift traffic to one completed route at a time, and monitor for any unexpected behavior.

Once you have iterated through all of your routes, congratulations! You've successfully migrated your monolith. You can shut down the underlying infrastructure, and refocus your ops efforts on improving performance for your customers.

## Contributing

Issue reports and pull requests to help improve these application templates are always welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License][mit-license].

[api-gateway]: https://aws.amazon.com/api-gateway/
[aws-sam-cli]: https://rbsttr.tv/samcli
[dynamodb]: https://aws.amazon.com/dynamodb/
[go]: https://golang.org
[http-api]: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html
[lambda]: https://aws.amazon.com/lambda/
[mit-license]: https://choosealicense.com/licenses/mit/
