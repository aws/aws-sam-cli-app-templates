# Cookiecutter Python Step Functions Sample App (Stock Trader) for SAM based Serverless App

A cookiecutter template to create a Python Step Functions Sample App (Stock Trader) boilerplate using [Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model).

This application creates a mock stock trading workflow which runs on a pre-defined schedule. It demonstrates the power of Step Functions to orchestrate Lambda functions and other AWS resources to form complex and robust workflows, coupled with event-driven development using Amazon EventBridge.

## Requirements

- [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli)

## Usage

- **python3.13**: `sam init --runtime python3.13 --app-template step-functions-with-connectors --name multi-step-app`

Access this template by running `sam init` and choosing it from the list of available templates.

# Credits

- This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
