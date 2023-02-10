# AWS SAM cookiecutter for .NET 6 with AWS Lambda Powertools for .NET

This [cookiecutter](https://github.com/audreyr/cookiecutter) creates a "Hello World" application using the AWS Serverless Application Model (AWS SAM) with the `dotnet6` runtime. This template provides options to bootstrap **AWS Lambda Powertools for .NET** utilities (Logging, Tracing and Metrics).

AWS Lambda Powertools for .NET (C#) is a suite of utilities for AWS Lambda functions to simplify implementation of serverless observability best practices such as tracing, structured logging, and custom metrics.

## Features

Lambda Powertools provides three core utilities:

* **[Logging](https://awslabs.github.io/aws-lambda-powertools-dotnet/core/logging/)** - provides a custom logger class that outputs structured JSON. It allows you to pass in strings or more complex objects, and will take care of serializing the log output. Common use cases—such as logging the Lambda event payload and capturing cold start information—are handled for you, including appending custom keys to the logger at anytime.

* **[Metrics](https://awslabs.github.io/aws-lambda-powertools-dotnet/core/metrics/)** - makes collecting custom metrics from your application simple, without the need to make synchronous requests to external systems. This functionality is powered by [Amazon CloudWatch Embedded Metric Format (EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html), which allows for capturing metrics asynchronously.

* **[Tracing](https://awslabs.github.io/aws-lambda-powertools-dotnet/core/tracing/)** - provides a simple way to send traces from functions to AWS X-Ray to provide visibility into function calls, interactions with other AWS services, or external HTTP requests. Annotations can easily be added to traces to allow filtering traces based on key information. For example, when using Tracer, a ColdStart annotation is created for you so you can easily group and analyze traces where there was an initialization overhead.

Visit the [documentation](https://awslabs.github.io/aws-lambda-powertools-dotnet/) for more information.

## Installation

The AWS Lambda Powertools for .NET utilities (.NET 6) are available as NuGet packages. You can install the packages from the NuGet gallery or from within the Visual Studio IDE. Search `AWS.Lambda.Powertools*` to see various utilities available. Powertools is available on NuGet.

* [AWS.Lambda.Powertools.Logging](https://www.nuget.org/packages?q=AWS.Lambda.Powertools.Logging):

    `dotnet add package AWS.Lambda.Powertools.Logging`

* [AWS.Lambda.Powertools.Metrics](https://www.nuget.org/packages?q=AWS.Lambda.Powertools.Metrics):

    `dotnet add package AWS.Lambda.Powertools.Metrics`

* [AWS.Lambda.Powertools.Tracing](https://www.nuget.org/packages?q=AWS.Lambda.Powertools.Tracing):

    `dotnet add package AWS.Lambda.Powertools.Tracing`

## Examples

We have provided examples focused specifically on each of the utilities. Each solution comes with an AWS Serverless Application Model (AWS SAM) templates to run your functions as a Zip package using the AWS Lambda .NET 6 managed runtime; or as a container package using the AWS base images for .NET.

* **[Logging example](examples/Logging/)**
* **[Metrics example](examples/Metrics/)**
* **[Tracing example](examples/Tracing/)**

# Cookiecutter Requirements

Please note, you should not try to `git clone` this project but use `cookiecutter` CLI instead as ``{{cookiecutter.project_name}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

Install `cookiecutter` command line:

**Pip users**:

* `pip install cookiecutter`

**Homebrew users**:

* `brew install cookiecutter`

**Windows or Pipenv users**:

* `pipenv install cookiecutter`

**NOTE**: [`Pipenv`](https://github.com/pypa/pipenv) is the new and recommended Python packaging tool that works across multiple platforms and makes Windows a first-class citizen.

## Usage

Generate a new SAM based Serverless App: `cookiecutter gh:aws-samples/cookiecutter-aws-sam-hello-dotnet`. 

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

**NOTE**: After you understand how cookiecutter works (cookiecutter.json, mainly), you can fork this repo and apply your own mechanisms to accelerate your development process and this can be followed for any programming language and OS.

# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)

# License

This project is licensed under the terms of the [MIT License with no attribution](/LICENSE)
