const cdk = require('@aws-cdk/core');
const lambda = require('@aws-cdk/aws-lambda')
const apigateway = require('@aws-cdk/aws-apigateway')
const path = require('path')

class AwsSamCliCdkHelloWorldStack extends cdk.Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const backend = new lambda.Function(this, 'hello-world-lambda-function', {
      runtime: lambda.Runtime.NODEJS_14_X,
      handler: 'app.lambdaHandler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'hello-world')),
    });

    const api = new apigateway.LambdaRestApi(this, 'hello-world-api', {
      handler: backend,
      proxy: false
    });

    const hello = api.root.addResource('hello');
    hello.addMethod('GET');
  }
}

module.exports = { AwsSamCliCdkHelloWorldStack }
