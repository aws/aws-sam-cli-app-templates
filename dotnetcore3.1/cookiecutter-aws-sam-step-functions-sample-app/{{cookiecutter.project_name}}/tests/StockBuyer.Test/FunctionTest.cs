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
            var request = new StockEvent { stockPrice = testStockPrice };
            var context = new TestLambdaContext();

            var function = new Function();
            var response = function.FunctionHandler(request, context);

            Assert.True(response.id is string);
            Assert.Equal(testStockPrice.ToString(), response.price);
            Assert.Equal("Buy", response.type);
            Assert.True(response.timestamp is string);
            int quantity;
            if(int.TryParse(response.qty, out quantity))
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