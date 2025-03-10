# AWS SAM cookiecutter for NodeJS TypeScript Lambda functions with Powertools for AWS Lambda (TypeScript)

**Please note, you should not try to `git clone` this project.** Instead, use `cookiecutter` CLI instead as ``{{cookiecutter.project_name}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

## Cookiecutter requirements

Install `cookiecutter` command line:

**Pip users**:

* `pip install cookiecutter`

**Homebrew users**:

* `brew install cookiecutter`

**Windows or Pipenv users**:

* `pipenv install cookiecutter`

**NOTE**: [`Pipenv`](https://github.com/pypa/pipenv) is the new and recommended Python packaging tool that works across multiple platforms and makes Windows a first-class citizen.

### Usage

Generate a new SAM based Serverless App: `sam init --runtime nodejs22.x`.

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

**NOTE**: After you understand how cookiecutter works (cookiecutter.json, mainly), you can fork this repo and apply your own mechanisms to accelerate your development process and this can be followed for any programming language and OS.

### Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)

### License

This project is licensed under the terms of the [MIT License with no attribution](/LICENSE)
