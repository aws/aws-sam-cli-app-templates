package StockSeller.src.test.java.stockSeller;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import java.util.HashMap;
import java.util.Map;
import org.junit.Test;
import StockSeller.src.main.java.stockSeller.App;

public class AppTest {

    @Test
    public void successfulResponse() {
        App app = new App();

        int stockPrice = 70;

        Map<String, Integer> event = new HashMap<>();
        event.put("stockPrice", stockPrice);

        Map<String, String> result = app.handleRequest(event, null);

        assertTrue(result.get("id") != null);
        assertEquals(String.valueOf(stockPrice), result.get("price"));
        assertEquals("Sell", result.get("type"));
        assertTrue(Integer.valueOf(result.get("qty")) > 0);
        assertTrue(Integer.valueOf(result.get("qty")) <= 10);
        assertTrue(result.get("timestamp") != null);
    }
}
