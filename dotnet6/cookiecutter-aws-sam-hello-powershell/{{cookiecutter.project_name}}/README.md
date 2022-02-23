# {{ cookiecutter.project_name }}

This project contains source code and supporting files for a serverless PowerShell function that you can deploy with the SAM CLI. It includes the following files and folders:

- src - Code for the PowerShell Lambda function.
- build.ps1 - build script that leverages AWSLambdaPSCore to compile and properly zip for Lambda.
- events - Invocation events that you can use to invoke the function.
- test - Unit tests for the function code.
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your function code.

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit.
The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started.

* [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## Requirements

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI with PowerShell, you need the following tools:

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [SAM CLI installed](https://github.com/awslabs/aws-sam-cli)
- [Docker installed](https://www.docker.com/community-edition)
- [.NET Core installed](https://www.microsoft.com/net/download)
- [PowerShell 7 installed](https://docs.microsoft.com/powershell/scripting/install/installing-powershell?view=powershell-7)
- [AWSLambdaPSCore PowerShell module](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-lambda.html)
- [Pester PowerShell module](https://github.com/pester/Pester)

## Use the SAM CLI to build and test locally

AWS Lambda PowerShell functions are compiled in to a .net core project before they are uploaded. Dependencies are detected through the `#Requires` statement in your script file. After your project is built SAM will use `CodeUri` property to know where to look for the built application (including its dependencies).

```yaml
...
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
            CodeUri: artifacts/Function.zip
```

To compile your PowerShell function to a .net core project for use within Lambda first run the following:

```powershell
PS {{ cookiecutter.project_name }}> .\build.ps1
```

This build script leverages AWSLambdaPSCore to properly detect `#Requires` dependencies and compile your PowerShell project into a zip that can be deployed to AWS Lambda as a .NET Core package bundle.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
{{ cookiecutter.project_name }}$ sam local invoke HelloWorldFunction
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
{{ cookiecutter.project_name }}$ sam local start-api
{{ cookiecutter.project_name }}$ curl http://localhost:3000/hello
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

## Add a resource to your application

The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
{{ cookiecutter.project_name }}$ sam logs -n HelloWorldFunction --stack-name {{ cookiecutter.project_name }} --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Unit tests

Tests are defined in the `test` folder in this project.

```powershell
PS {{ cookiecutter.project_name }}> Invoke-Pester
```

This will run all files that end in `tests.ps1` in the test directory.

## Packaging and deployment

[Configure your AWS credentials](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-set-up-credentials.html) for authenticated access to your AWS account.

```bash
$ aws configure
```

An `S3 bucket` is required to upload the Lambda functions packaged as ZIP. If you don't have a S3 bucket to store code artifacts then this is a good time to create one:

```bash
$ aws s3 mb s3://BUCKET_NAME
```

Next, run the following command to package our Lambda function to S3:

```bash
sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME
```

Next, the following command will create a Cloudformation Stack and deploy your SAM resources.

```bash
sam deploy \
    --template-file packaged.yaml \
    --stack-name {{ cookiecutter.project_name.lower().replace(' ', '-') }} \
    --capabilities CAPABILITY_IAM
```

> **See [Serverless Application Model (SAM) HOWTO Guide](https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md) for more details in how to get started.**

After deployment is complete you can run the following command to retrieve the API Gateway Endpoint URL:

```bash
aws cloudformation describe-stacks \
    --stack-name {{ cookiecutter.project_name.lower().replace(' ', '-') }} \
    --query 'Stacks[].Outputs[?OutputKey==`HelloWorldApi`]' \
    --output table
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name {{ cookiecutter.project_name }}
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)


## QuickStart Reference

```powershell
# compile your PowerShell project into a zip that can be deployed
PS {{ cookiecutter.project_name }}> .\build.ps1
```

```bash
# Invoke function locally
{{ cookiecutter.project_name }}$ sam local invoke HelloWorldFunction

# Invoke function locally and capture Lambda outputs to log file
{{ cookiecutter.project_name }}$ sam local invoke HelloWorldFunction --log-file logoutput.txt

# Invoke function locally with event.json as an input
{{ cookiecutter.project_name }}$ sam local invoke HelloWorldFunction --event event.json

# Run API Gateway locally
{{ cookiecutter.project_name }}$ sam local start-api

# Interact with your local API \
curl http://localhost:3000/hello

# Create S3 bucket
aws s3 mb s3://BUCKET_NAME

# Package Lambda function defined locally and upload to S3 as an artifact
sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME

# Deploy SAM template as a CloudFormation stack
sam deploy \
    --template-file packaged.yaml \
    --stack-name {{ cookiecutter.project_name.lower().replace(' ', '-') }} \
    --capabilities CAPABILITY_IAM

# Describe Output section of CloudFormation stack previously created
aws cloudformation describe-stacks \
    --stack-name {{ cookiecutter.project_name.lower().replace(' ', '-') }} \
    --query 'Stacks[].Outputs[?OutputKey==`HelloWorldApi`]' \
    --output table

# Tail Lambda function Logs using Logical name defined in SAM Template
sam logs -n HelloWorldFunction --stack-name {{ cookiecutter.project_name.lower().replace(' ', '-') }} --tail

```
