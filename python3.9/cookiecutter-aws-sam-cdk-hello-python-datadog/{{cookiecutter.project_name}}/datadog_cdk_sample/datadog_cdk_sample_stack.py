import aws_cdk as cdk
from constructs import Construct
from aws_cdk import aws_lambda as lambda_

from datadog_cdk_constructs_v2 import Datadog

import os

class DatadogCDKSampleStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        function = lambda_.Function(self, "test-lambda", 
                                       runtime=lambda_.Runtime.PYTHON_3_7,
                                       handler="handler.main",
                                       code=lambda_.Code.from_asset("./lambda"))

        datadog = Datadog(self, "Datadog",
                          python_layer_version=50,
                          extension_layer_version=16,
                          api_key=os.environ.get("API_KEY"))

        datadog.add_lambda_functions([function])