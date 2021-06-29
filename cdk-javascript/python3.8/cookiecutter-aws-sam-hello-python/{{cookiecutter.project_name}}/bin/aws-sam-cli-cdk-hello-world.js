#!/usr/bin/env node

const cdk = require('@aws-cdk/core');
const { AwsSamCliCdkHelloWorldStack } = require('../lib/aws-sam-cli-cdk-hello-world-stack');

const app = new cdk.App();
new AwsSamCliCdkHelloWorldStack(app, '{{ cookiecutter.project_name }}');