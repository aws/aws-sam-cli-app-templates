# Cookiecutter Ruby Hello-world for SAM based Serverless App

A cookiecutter template to create a Ruby Hello world boilerplate using [Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model).

## Requirements

* [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli)

## Usage

Generate a boilerplate template in your current project directory using the following syntax:

* **Ruby {{ cookiecutter.options[cookiecutter.runtime].version }}**: `sam init --runtime {{ cookiecutter.runtime }}`

> **NOTE**: ``--name`` allows you to specify a different project folder name (`sam-app` is the default)


# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
