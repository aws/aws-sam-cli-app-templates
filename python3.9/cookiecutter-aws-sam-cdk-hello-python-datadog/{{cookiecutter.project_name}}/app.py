#!/usr/bin/env python3
import os

import aws_cdk as cdk

from datadog_cdk_sample.datadog_cdk_sample_stack import DatadogCDKSampleStack


app = cdk.App()
DatadogCDKSampleStack(app, {{cookiecutter.project_name}}, 
                    env=cdk.Environment(
                        account=os.environ["CDK_DEFAULT_ACCOUNT"],
                        region="sa-east-1"
                    ))

app.synth()
