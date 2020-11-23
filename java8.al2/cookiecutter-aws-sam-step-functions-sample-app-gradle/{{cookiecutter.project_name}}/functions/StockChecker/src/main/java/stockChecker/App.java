package StockChecker.src.main.java.stockChecker;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<Map<String, String>, Map<String, Integer>> {
    private final Random rand = new Random();

    public Map<String, Integer> handleRequest(Map<String, String> event, Context context) {
        // Sample Lambda function which mocks the operation of checking the current price
        // of a stock.

        // For demonstration purposes this Lambda function simply returns
        // a random integer between 0 and 100 as the stock price.

        // Parameters
        // ----------
        // event: Map<String, String>, required
        //     Input event to the Lambda function

        // context: Context, required
        //     Lambda Context runtime methods and attributes

        // Returns
        // ------
        //     Map<String, Integer>: Object containing the current price of the stock

        Map<String, Integer> response = new HashMap<>();
        response.put("stockPrice", rand.nextInt(100));

        return response;
    }
}
