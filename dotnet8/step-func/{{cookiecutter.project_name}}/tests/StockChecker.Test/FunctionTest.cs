using Amazon.Lambda.TestUtilities;
using Xunit;

namespace StockChecker.Tests;

public class FunctionTest
{

  [Fact]
  public void TestStockCheckerFunctionHandler()
  {
          var context = new TestLambdaContext();

          var function = new Function();
          var response = function.FunctionHandler(context);

          Assert.True(response.StockPrice >= 0);
          Assert.True(response.StockPrice <= 99);
  }
}