# Cookiecutter SAM for golang Lambda functions

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a Serverless App based on Serverless Application Model (SAM).

It is important to note that you should not try to `git clone` this project but use `cookiecutter` CLI instead as ``\\{\\{cookiecutter.project_slug\\}\\}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

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

Generate a boilerplate template in your current project directory using the following syntax:

* `sam init`


> **NOTE**: ``--name`` allows you to specify a different project folder name (`sam-app` is the default)

## Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)

## License

This project is licensed under the terms of the [MIT License with no attribution](/LICENSE)
