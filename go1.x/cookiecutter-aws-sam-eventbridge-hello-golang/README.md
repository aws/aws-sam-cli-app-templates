# Cookiecutter SAM for Golang Lambda functions

This is a static [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a Serverless EventBridge Hello World App based on Serverless Application Model (SAM) and Golang.

It is important to note that you should not try to `git clone` this project but use `cookiecutter` CLI instead as ``{{cookiecutter.project_name}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

This template creates a Serverless Application that reacts to EC2 Instance State change events, demonstrating the power of event-driven development with Amazon EventBridge.
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

Access this template by running `sam init` and choosing it from the list of available templates


## Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [Bruno Alla's Lambda function template](https://github.com/browniebroke/cookiecutter-lambda-function)

## License

This project is licensed under the terms of the [MIT License with no attribution](/LICENSE)