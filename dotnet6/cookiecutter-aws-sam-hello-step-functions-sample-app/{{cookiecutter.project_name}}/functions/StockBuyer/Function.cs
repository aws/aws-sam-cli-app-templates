using Amazon.Lambda.Core;
using System;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace StockBuyer
{
    public class StockEvent
    {
        public int stockPrice;
    }

    public class TransactionResult
    {
        public string id;
        public string price;
        public string type;
        public string qty;
        public string timestamp;
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
                id = rand.Next().ToString(),
                type = "Buy",
                price = stockEvent.stockPrice.ToString(),
                qty = (rand.Next() % 10 + 1).ToString(),
                timestamp = DateTime.Now.ToString("yyyyMMddHHmmssffff")
            };
        }
    }
}
