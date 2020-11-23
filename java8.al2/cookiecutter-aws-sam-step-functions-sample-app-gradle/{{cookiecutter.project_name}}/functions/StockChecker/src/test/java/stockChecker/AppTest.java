package StockChecker.src.test.java.stockChecker;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import java.util.Map;
import org.junit.Test;
import StockChecker.src.main.java.stockChecker.App;

public class AppTest {

    @Test
    public void successfulResponse() {
        App app = new App();

        Map<String, Integer> result = app.handleRequest(null, null);

        assertTrue(result.get("stockPrice") >= 0);
        assertTrue(result.get("stockPrice") < 100);
    }
}
