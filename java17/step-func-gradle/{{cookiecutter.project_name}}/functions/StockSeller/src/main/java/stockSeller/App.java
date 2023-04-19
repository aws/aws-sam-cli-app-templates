package StockSeller.src.main.java.stockSeller;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.UUID;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<Map<String, Integer>, Map<String, String>> {
    private final java.util.Random rand = new Random();

    public Map<String, String> handleRequest(Map<String, Integer> event, Context context) {
    // Sample Lambda function which mocks the operation of selling a random number
    // of shares for a stock.

    // For demonstration purposes, this Lambda function does not actually perform any
    // actual transactions. It simply returns a mocked result.

    // Parameters
    // ----------
    // event: Map<String, String>, required
    //     Input event to the Lambda function

    // context: Context, required
    //     Lambda Context runtime methods and attributes

    // Returns
    // ------
    //     Map<String, String>: Object containing details of the stock selling transaction

        Map<String, String> response = new HashMap<>();
        response.put("id", UUID.randomUUID().toString());
        response.put("price", String.valueOf(event.get("stockPrice")));
        response.put("type", "Sell");
        response.put("qty", String.valueOf(rand.nextInt(10) + 1));
        response.put("timestamp", java.time.LocalDateTime.now().toString());

        return response;
    }
}
