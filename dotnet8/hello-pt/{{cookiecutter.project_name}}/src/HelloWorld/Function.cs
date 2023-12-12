using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Net.Http;
using System.Text.Json;

using Amazon.Lambda.Core;
using Amazon.Lambda.APIGatewayEvents;
{%- if cookiecutter["Powertools for AWS Lambda (.NET) Tracing"] == "enabled"%}
using AWS.Lambda.Powertools.Tracing;
{%- endif %}
{%- if cookiecutter["Powertools for AWS Lambda (.NET) Metrics"] == "enabled"%}
using AWS.Lambda.Powertools.Metrics;
{%- endif %}
{%- if cookiecutter["Powertools for AWS Lambda (.NET) Logging"] == "enabled"%}
using AWS.Lambda.Powertools.Logging;
{%- endif %}

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace HelloWorld
{
    public class Function
    {
        private static readonly HttpClient client = new HttpClient();
        
        {%- if cookiecutter["Powertools for AWS Lambda (.NET) Tracing"] == "enabled"%}
        public Function()
        {
            Tracing.RegisterForAllServices();
        }
        {%- endif %}
  
        {%- if cookiecutter["Powertools for AWS Lambda (.NET) Tracing"] == "enabled"%}
        [Tracing(SegmentName = "Get Calling IP")]
        {%- endif %}
        private static async Task<string> GetCallingIP()
        {
            try
            {
                client.DefaultRequestHeaders.Accept.Clear();
                client.DefaultRequestHeaders.Add("User-Agent", "AWS Lambda .Net Client");

                var msg = await client.GetStringAsync("http://checkip.amazonaws.com/").ConfigureAwait(continueOnCapturedContext:false);

                {%- if cookiecutter["Powertools for AWS Lambda (.NET) Metrics"] == "enabled"%}
                // Custom Metric
                // https://awslabs.github.io/aws-lambda-powertools-dotnet/core/metrics/
                Metrics.AddMetric("ApiRequestCount", 1, MetricUnit.Count);
                {%- endif %}

                return msg.Replace("\n","");
            }
            catch (Exception ex)
            {
                {%- if cookiecutter["Powertools for AWS Lambda (.NET) Logging"] == "enabled" %}
                Logger.LogError(ex);
                {%- endif %}
                throw;
            }
        }

         
        {%- if cookiecutter["Powertools for AWS Lambda (.NET) Tracing"] == "enabled"%}
        [Tracing(CaptureMode = TracingCaptureMode.ResponseAndError)]
        {%- endif %}
        {%- if cookiecutter["Powertools for AWS Lambda (.NET) Metrics"] == "enabled"%}
        [Metrics(CaptureColdStart = true)]
        {%- endif %}
        {%- if cookiecutter["Powertools for AWS Lambda (.NET) Logging"] == "enabled"%}
        [Logging(CorrelationIdPath = CorrelationIdPaths.ApiGatewayRest)]
        {%- endif %}
        public async Task<APIGatewayProxyResponse> FunctionHandler(APIGatewayProxyRequest apigProxyEvent, ILambdaContext context)
        {

            var location = await GetCallingIP();
            var body = new Dictionary<string, string>
            {
                { "message", "hello world" },
                { "location", location }
            };

            {%- if cookiecutter["Powertools for AWS Lambda (.NET) Logging"] == "enabled" %}
            // Structured logging
            // https://awslabs.github.io/aws-lambda-powertools-dotnet/core/logging/
            Logger.LogInformation("Hello world API - HTTP 200");
            {%- endif %}

            return new APIGatewayProxyResponse
            {
                Body = JsonSerializer.Serialize(body),
                StatusCode = 200,
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
            };
        }
    }
}
