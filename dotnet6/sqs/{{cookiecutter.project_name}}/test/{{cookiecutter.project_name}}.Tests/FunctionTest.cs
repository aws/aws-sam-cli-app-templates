using Xunit;
using Amazon.Lambda.TestUtilities;
using Amazon.Lambda.SQSEvents;

using {{cookiecutter.project_name}};

namespace {{cookiecutter.project_name}}.Tests
{
    public class FunctionTest
    {
        [Fact]
        public async Task TestSQSEventLambdaFunction()
        {
            var sqsEvent = new SQSEvent
            {
                Records = new List<SQSEvent.SQSMessage>
                {
                    new SQSEvent.SQSMessage
                    {
                        Body = "foobar"
                    }
                }
            };

            var logger = new TestLambdaLogger();
            var context = new TestLambdaContext
            {
                Logger = logger
            };

            var function = new Function();
            await function.FunctionHandler(sqsEvent, context);

            Assert.Contains("Processed message foobar", logger.Buffer.ToString());
        }
    }
}
