# Cookiecutter Python Scheduled Events for SAM based Serverless App

A cookiecutter template to create a Python boilerplate for a Lambda function triggered on a schedule, using [Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model).

This template creates a Serverless Application with a Lambda function that runs every hour through an Amazon EventBridge schedule rule and logs the event payload.

## Requirements

- [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli)

## Usage

Generate a boilerplate template in your current project directory using the following syntax:

- **Python 3.10**: `sam init --runtime python3.10 --app-template quick-start-cloudwatch-events`

> **NOTE**: `--name` allows you to specify a different project folder name (`sam-app` is the default)

# Credits

- This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
