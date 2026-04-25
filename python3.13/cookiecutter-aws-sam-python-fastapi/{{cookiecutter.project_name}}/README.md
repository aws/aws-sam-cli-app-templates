# {{cookiecutter.project_name}}

This is a FastAPI application deployed as an AWS Lambda function using the Mangum adapter.

## Requirements
* AWS CLI
* SAM CLI
* Python 3.13 installed

## Local Development
1. Install dependencies: `pip install -r app/requirements.txt`
2. Run locally: `sam local start-api`