using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Xunit;
using Amazon.Lambda.Core;
using Amazon.Lambda.TestUtilities;
using Amazon.Lambda.CloudWatchEvents;

using {{cookiecutter.project_name}};

namespace {{cookiecutter.project_name}}.Tests
{
    public class FunctionTest
    {
        [Fact]
        public void TestToUpperFunction()
        {

            // Invoke the lambda function and confirm the string was upper cased.
            var function = new Function();
            var context = new TestLambdaContext();
            var eventPayload = new CloudWatchEvent<dynamic>()
            {
                Id = "cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
                DetailType = "Scheduled Event",
                Source = "aws.events",
                Account = "",
                Time = Convert.ToDateTime("1970-01-01T00:00:00Z"),
                Region = "us-west-2",
                Resources = new List<string>() { "arn:aws:events:us-west-2:123456789012:rule/ExampleRule" },
                Detail = new { }
            };

            var functionResult = function.FunctionHandler(eventPayload, context);

            Assert.Equal("Done", functionResult);
        }
    }
}
