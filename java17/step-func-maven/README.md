# Cookiecutter Java Step Functions Sample App (Stock Trader) for SAM based Serverless App

A cookiecutter template to create a Java Step Functions Sample App (Stock Trader) boilerplate using [Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model).

This application creates a stock trading workflow which runs on a pre-defined schedule. It demonstrates the power of Step Functions to orchestrate Lambda functions and other AWS resources to form complex and robust workflows, coupled with event-driven development using Amazon EventBridge.

## Requirements

Install `cookiecutter` command line:

**Pip users**:

* `pip install cookiecutter`

**Homebrew users**:

* `brew install cookiecutter`

**Windows or Pipenv users**:

* `pipenv install cookiecutter`

**NOTE**: [`Pipenv`](https://github.com/pypa/pipenv) is the new and recommended Python packaging tool that works across multiple platforms and makes Windows a first-class citizen.

## Usage

Generate a new SAM based Serverless App: `cookiecutter gh:aws-samples/cookiecutter-aws-sam-hello-java`.

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

**NOTE**: After you understand how cookiecutter works (cookiecutter.json, mainly), you can fork this repo and apply your own mechanisms to accelerate your development process and this can be followed for any programming language and OS.

# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
