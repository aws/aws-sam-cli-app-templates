# Cookiecutter Python Hello-world for Kinesis event sources

A cookiecutter template to create a Python Hello world boilerplate using [Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model).

This template creates a Serverless Application that starts a Glue job and then invokes another function after either successful or failed job execution.


## Requirements

* [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli)


## Usage

Generate a boilerplate template in your current project directory using the following syntax:

* **Python 3.9**: `sam init --runtime python3.9`

> **NOTE**: ``--name`` allows you to specify a different project folder name (`sam-app` is the default)


# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
