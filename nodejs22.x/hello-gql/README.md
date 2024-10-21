# {{ cookiecutter.project_name }}

This is a sample template for {{ cookiecutter.project_name }} - Below is a brief explanation of what we have generated for you:

```bash
.
├── README.md                   <-- This instructions file
├── gql                         <-- Source code for schema and pipeline functions
│   ├── createPostItem.js       <-- Pipeline function code
│   ├── getPostFromTable.js     <-- Pipeline function code
│   ├── greet.js                <-- Pipeline function code
│   ├── preprocessPostItem.js   <-- Pipeline function code
│   └── schema.graphql          <-- Schema definition
├── greeter                     <-- Source code for lambda function
│   ├── tests                   <-- Tests for lambda function
│   │   ├──events               <-- Event stubs
│   │   │  └── appsync.json     <-- Sample event for tests
│   │   └──unit                 <-- Unit tests
│   │      └── test-handler.mjs <-- Source file with tests
│   ├── app.mjs                 <-- Lambda function source code
│   └── package.json            <-- List of Lambda dependencies and npm scripts
└── template.yaml               <-- SAM template
```

## Requirements

* AWS CLI already configured with Administrator permission
* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## Deploy the sample application

To deploy your application for the first time, run the following in your shell:

```bash
sam deploy --guided
```

This command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your AppSync GraphQL Endpoint URL and API key, which is required to access your API, in the output values displayed after deployment.

## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name "{{ cookiecutter.__stack_name }}"
```

## Test lambda function locally

1. Open terminal in `{{ cookiecutter.__stack_name }}/greeter` directory
2. Run `npm i`
3. Run `npm run test`

To modify the lambda function event, edit `{{ cookiecutter.__stack_name }}/greeter/tests/events/appsync.json` file.

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.
