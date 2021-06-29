#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { AwsSamCliCdkHelloWorldStack } from '../lib/aws-sam-cli-cdk-hello-world-stack';

const app = new cdk.App();
new AwsSamCliCdkHelloWorldStack(app, '{{ cookiecutter.project_name }}');
