using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Xunit;
using Amazon.Lambda.TestUtilities;

namespace HelloWorld.Tests
{
    public class FunctionTest
    {

        [Fact]
        public async Task TestHelloWorldFunctionHandler()
        {
            var input = "Hello World";
            var context = new TestLambdaContext();

            var expectedResponse = "HELLO WORLD";

            var function = new Function();
            var expectedResponse = function.FunctionHandler(input, context);


            Assert.Equal(expectedResponse, expectedResponse);
        }
    }
}