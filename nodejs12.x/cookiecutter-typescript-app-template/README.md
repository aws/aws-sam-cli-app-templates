# {{ cookiecutter.project_name }}

This template generates a sample NodeJS 12.x project configured with TypeScript using the [Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model).

This template includes a full suite of tests using [MochaJs](https://mochajs.org/), [ChaiJs](https://www.chaijs.com/) and mocking of services using [Moq.ts](https://github.com/dvabuzyarov/moq.ts). The project is configured to lint the TypeScript using [eslint](https://eslint.org/).

## Requirements

* [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli)
* 
## ## Usage

Generate a boilerplate tempalte in your current project directory using the following syntax:

```
$ sam init --runtime nodejs12.x
```

> **NOTE**: ``--name`` allows you to specify a different project folder name (`sam-app` is the default)

Once the template is generated and you have installed the dependencies via `$ npm install` you can run the unit tests, lint the project and compile the project with the following NPM scripts.

```
$ npm run compile
$ npm run test
$ npm run lint
```

Both the `compile` and the `test` commands will _always_ run the `lint` process. If you want to skip linting during compilation of testing you can use the `fast-compile` or the `fast-test` commands instead.

## Deployment

In order to deploy via the SAM CLI you will need to first run the `$ npm run compile` command. All of the TypeScript files under `/src` will be transpiled to JavaScript and placed into the `/dist` directory. The SAM Template uses this directory to provide the Lambda functions with the handler source code.

It is recommended that you run `$ npm prune --production` before you execute the SAM deployment process to remove all dev dependencies and reduce your overall Lambda size. The following is an example deployment process.

```
$ npm install
$ npm run compile
$ npm prune --production
sam deploy \
    --template-file template.yml \
    --stack-name myapp-dev-todoapi \
    --s3-bucket myapp-dev-deployments \
    --s3-prefix todoapi \
    --capabilities CAPABILITY_NAMED_IAM
    
# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)