using Amazon.Lambda.TestUtilities;
using Xunit;

namespace StockBuyer.Tests
{
  public class FunctionTest
  {

    [Fact]
    public void TestStockBuyerFunctionHandler()
    {
            var testStockPrice = 34;
            var request = new StockEvent { StockPrice = testStockPrice };
            var context = new TestLambdaContext();

            var function = new Function();
            var response = function.FunctionHandler(request, context);

            Assert.True(response.Id is string);
            Assert.Equal(testStockPrice.ToString(), response.Price);
            Assert.Equal("Buy", response.Type);
            Assert.True(response.Timestamp is string);
            int quantity;
            if(int.TryParse(response.Qty, out quantity))
            {
              Assert.True(quantity >= 1);
              Assert.True(quantity <= 10);
            }
            else
            {
              Assert.True(false, "Quantity was not a valid number.");
            }

    }
  }
}