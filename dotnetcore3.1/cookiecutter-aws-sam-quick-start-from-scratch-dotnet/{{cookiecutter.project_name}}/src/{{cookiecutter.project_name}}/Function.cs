using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Amazon.Lambda.Core;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace {{cookiecutter.project_name}}
{
    public class Function
    {
        
        /// <summary>
        /// A simple function that takes a string and does a ToUpper
        /// </summary>
        /// <param name="input"></param>
        /// <param name="context"></param>
        /// <returns></returns>
        public string FunctionHandler(string input, ILambdaContext context)
        {
            var message = input ?? "Hello from Lambda!";
            // All log statements are written to CloudWatch by default. For more information, see
            // https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-logging.html
            context.Logger.LogLine($"Processed message: {message}");
            return message.ToUpper();
        }
    }
}
