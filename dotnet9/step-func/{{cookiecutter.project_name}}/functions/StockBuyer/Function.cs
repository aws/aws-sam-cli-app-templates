using Amazon.Lambda.Core;
using System;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.CamelCaseLambdaJsonSerializer))]

namespace StockBuyer;

public class StockEvent
{
    public int StockPrice { get; set; }
}

public class TransactionResult
{
    public string Id { get; set; } = string.Empty;
    public string Price { get; set; } = string.Empty;
    public string Type { get; set; } = string.Empty;
    public string Qty { get; set; } = string.Empty;
    public string Timestamp { get; set; } = string.Empty;
}

public class Function
{

    private static readonly Random rand = new Random((Int32)(DateTime.UtcNow.Subtract(new DateTime(1970, 1, 1))).TotalSeconds);

    public TransactionResult FunctionHandler(StockEvent stockEvent, ILambdaContext context)
    {
        // Sample Lambda function which mocks the operation of buying a random number
        // of shares for a stock.

        // For demonstration purposes, this Lambda function does not actually perform any
        // actual transactions. It simply returns a mocked result.

        // Parameters
        // ----------
        // stockEvent: StockEvent, required
        //     Input event to the Lambda function

        // context: ILambdaContext
        //     Lambda Context runtime methods and attributes

        // Returns
        // ------
        //     TransactionResult: Object containing details of the stock buying transaction

        return new TransactionResult
        {
            Id = rand.Next().ToString(),
            Type = "Buy",
            Price = stockEvent.StockPrice.ToString(),
            Qty = (rand.Next() % 10 + 1).ToString(),
            Timestamp = DateTime.Now.ToString("yyyyMMddHHmmssffff")
        };
    }
}