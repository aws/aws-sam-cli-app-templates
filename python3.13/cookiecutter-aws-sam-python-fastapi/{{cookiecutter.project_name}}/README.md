# {{cookiecutter.project_name}}

This is a FastAPI application deployed as an AWS Lambda function using the Mangum adapter.

## Requirements
* AWS CLI
* SAM CLI
* Python 3.13 installed
* Docker

## Local Development
1. Build the application: `sam build`
2. Run locally: `sam local start-api`
3. Open `http://127.0.0.1:3000/`

## Deploy the application

```bash
sam build
sam deploy --guided
```

## Run unit tests

Install the application dependencies and test dependencies, then run pytest.

```bash
python -m pip install -r app/requirements.txt pytest pytest-mock
python -m pytest tests/unit
```