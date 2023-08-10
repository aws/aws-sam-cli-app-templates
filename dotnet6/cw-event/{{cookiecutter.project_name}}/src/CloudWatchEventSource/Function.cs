using System.Text.Json;

using Amazon.Lambda.Core;
using Amazon.Lambda.CloudWatchEvents;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace CloudWatchEventSource;

public class Function
{
    
    /// <summary>
    /// A simple function that takes a string and does a ToUpper
    /// </summary>
    /// <param name="evnt"></param>
    /// <param name="context"></param>
    /// <returns></returns>
    public string FunctionHandler(CloudWatchEvent<dynamic> evnt, ILambdaContext context)
    {
        // All log statements are written to CloudWatch by default. For more information, see
        // https://docs.aws.amazon.com/lambda/latest/dg/csharp-logging.html
        context.Logger.LogLine(JsonSerializer.Serialize(evnt));
        return "Done";
    }
}
