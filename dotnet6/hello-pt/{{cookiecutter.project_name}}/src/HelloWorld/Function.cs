using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Net.Http;
using System.Text.Json;

using Amazon.Lambda.Core;
using Amazon.Lambda.APIGatewayEvents;
{%- if cookiecutter["Powertools Tracing"] == "enabled"%}
using Amazon.XRay.Recorder.Handlers.AwsSdk;
using AWS.Lambda.Powertools.Tracing;
{%- endif %}
{%- if cookiecutter["Powertools Metrics"] == "enabled"%}
using AWS.Lambda.Powertools.Metrics;
{%- endif %}
{%- if cookiecutter["Powertools Logging"] == "enabled"%}
using AWS.Lambda.Powertools.Logging;
{%- endif %}

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace HelloWorld
{

    public class Function
    {
        {%- if cookiecutter["Powertools Tracing"] == "enabled"%}
        AWSSDKHandler.RegisterXRayForAllServices();
        {%- endif %}
        private static readonly HttpClient client = new HttpClient();

        {%- if cookiecutter["Powertools Tracing"] == "enabled"%}
        [Tracing(SegmentName = "Get Calling IP")]
        {%- endif %}
        private static async Task<string> GetCallingIP()
        {
            client.DefaultRequestHeaders.Accept.Clear();
            client.DefaultRequestHeaders.Add("User-Agent", "AWS Lambda .Net Client");

            var msg = await client.GetStringAsync("http://checkip.amazonaws.com/").ConfigureAwait(continueOnCapturedContext:false);

            return msg.Replace("\n","");
        }

        {%- if cookiecutter["Powertools Tracing"] == "enabled"%}
        [Tracing(CaptureMode = TracingCaptureMode.ResponseAndError)]
        {%- endif %}
        {%- if cookiecutter["Powertools Metrics"] == "enabled"%}
        [Metrics(CaptureColdStart = true)]
        {%- endif %}
        {%- if cookiecutter["Powertools Logging"] == "enabled"%}
        [Logging(LogEvent = true)]
        {%- endif %}
        public async Task<APIGatewayProxyResponse> FunctionHandler(APIGatewayProxyRequest apigProxyEvent, ILambdaContext context)
        {

            var location = await GetCallingIP();
            var body = new Dictionary<string, string>
            {
                { "message", "hello world" },
                { "location", location }
            };

            return new APIGatewayProxyResponse
            {
                Body = JsonSerializer.Serialize(body),
                StatusCode = 200,
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
            };
        }
    }
}
