# {{ cookiecutter.project_name }}

This template generates a sample NodeJS 12.x project configured with TypeScript using the [Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model).

This template includes a full suite of tests using [MochaJs](https://mochajs.org/), [ChaiJs](https://www.chaijs.com/) and mocking of services using [Moq.ts](https://github.com/dvabuzyarov/moq.ts). The project is configured to lint the TypeScript using [eslint](https://eslint.org/).

## Requirements

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)
* GNU Make
    * On Windows, you can use [Chocolatey](https://chocolatey.org/) to install Make by running `choco install make`

Once the template is generated, and you have installed the dependencies via `$ npm install` you can run the unit tests, lint the project and compile the project with the following NPM scripts.

```
$ npm run compile
$ npm run test
$ npm run lint
```

Both the `compile` and the `test` commands will _always_ run the `lint` process. If you want to skip linting during compilation of testing you can use the `fast-compile` or the `fast-test` commands instead.

## Deploy the sample application

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

The first command will build the source of your application. This template is configured to use `make` for the build process.

The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
