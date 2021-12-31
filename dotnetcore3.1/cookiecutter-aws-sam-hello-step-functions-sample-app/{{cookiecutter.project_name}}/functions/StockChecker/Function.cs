using System;
using Amazon.Lambda.Core;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace StockChecker
{
    public class StockEvent
    {
        public int stockPrice { get; set; }
    }

    public class Function
    {

        private static readonly Random rand = new Random((Int32)(DateTime.UtcNow.Subtract(new DateTime(1970, 1, 1))).TotalSeconds);

        public StockEvent FunctionHandler(ILambdaContext context)
        {
            // Sample Lambda function which mocks the operation of checking the current price
            // of a stock.

            // For demonstration purposes this Lambda function simply returns
            // a random integer between 0 and 100 as the stock price.

            // Parameters
            // ----------
            // context: ILambdaContext
            //     Lambda Context runtime methods and attributes

            // Returns
            // ------
            //     StockEvent: Object containing the current price of the stock

            return new StockEvent
            {
                stockPrice = rand.Next() % 100
            };
        }
    }
}
