# Cookiecutter NodeJS Step Functions Sample App (Stock Trader) for SAM based Serverless App

A cookiecutter template to create a NodeJS Step Functions Sample App (Stock Trader) boilerplate using 
[Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model).

This application creates a mock stock trading workflow which runs on a pre-defined schedule. It demonstrates the power of Step Functions to orchestrate Lambda functions and other AWS resources to form complex and robust workflows, coupled with event-driven development using Amazon EventBridge.

## Requirements

* [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli)

## Usage

Generate a boilerplate template in your current project directory using the following syntax:

* **NodeJS 14**: `sam init --runtime nodejs14.x`

> **NOTE**: ``--name`` allows you to specify a different project folder name (`sam-app` is the default)

# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)

