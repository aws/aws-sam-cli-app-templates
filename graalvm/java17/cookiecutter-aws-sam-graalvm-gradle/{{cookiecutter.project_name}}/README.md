# {{ cookiecutter.project_name }}

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes [Lambda Powertools for operational best practices](https://github.com/awslabs/aws-lambda-powertools-java), and the following files and folders.

- HelloWorldFunction/src/main - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- HelloWorldFunction/src/test - Unit tests for the application code.
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit.  
The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started.

- [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
- [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## GraalVM

This sample uses GraalVM to create a native binary of your Java application. By compiling Java to a native executable the performance is increased and cold-start is reduced.

This sample contains build configurations for both Maven and Gradle build systems. (See Makefile in HelloWorldFunction)

A docker image is required to compile for the Lambda execution environment (based on Amazon Linux 2). This image can be built using the `build.sh` script or by executing the following command in your shell:

```bash
docker build -t al2-graalvm .
```

This image is then used when building the SAM package:

```bash
sam build --use-container --build-image al2-graalvm
```

**Note:**

Some configuration files are required to compiled to a native binary. These files are located in `src/resources/META-INF` folder. Adjust the `src/resources/META-INF/helloworld/reflect-config.json` file to support your classes accordingly. If this file is not configured to match your handler, the Lambda Runtime Interface Client (RIC) won't be able to find your handler and throw a `ClassNotFoundException`

Also keep in mind the the Lambda events classes needs to be recognized by GraalVM to not throw the aforementioned exception.

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

- SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Java11 - [Install the Java 11](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html)
- Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
{{ cookiecutter.project_slug }}$ sam build
{{ cookiecutter.project_slug }}$ sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

- **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
- **AWS Region**: The AWS region you want to deploy your app to.
- **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
- **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modified IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
- **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
{{ cookiecutter.project_slug }}$ sam build
```

The SAM CLI installs dependencies defined in `HelloWorldFunction/pom.xml`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
{{ cookiecutter.project_slug }}$ sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
{{ cookiecutter.project_slug }}$ sam local start-api
{{ cookiecutter.project_slug }}$ curl http://localhost:3000/
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
{{ cookiecutter.project_slug }}$ sam logs -n HelloWorldFunction --stack-name <Name-of-your-deployed-stack> --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Unit tests

Tests are defined in the `HelloWorldFunction/src/test` folder in this project.

```bash
{{ cookiecutter.project_slug }}$ cd HelloWorldFunction
HelloWorldFunction$ mvn test
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name <Name-of-your-deployed-stack>
```

# Appendix

## Powertools

**Tracing**

[Tracing utility](https://awslabs.github.io/aws-lambda-powertools-java/core/tracing/) provides functionality to reduce the overhead of performing common tracing tasks. It traces the execution of this sample code including the response and exceptions as tracing metadata - You can visualize them in AWS X-Ray.

**Logger**

[Logging utility](https://awslabs.github.io/aws-lambda-powertools-java/core/logging/) creates an opinionated application Logger with structured logging as the output, dynamically samples a percentage (samplingRate) of your logs in DEBUG mode for concurrent invocations, log incoming events as your function is invoked, and injects key information from Lambda context object into your Logger - You can visualize them in Amazon CloudWatch Logs.

**Metrics**

[Metrics utility](https://awslabs.github.io/aws-lambda-powertools-java/core/metrics/) captures cold start metric of your Lambda invocation, and could add additional metrics to help you understand your application KPIs - You can visualize them in Amazon CloudWatch.

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Check the [AWS Lambda Powertools Java](https://awslabs.github.io/aws-lambda-powertools-java/) for more information on how to use and configure such tools

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
