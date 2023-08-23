package helloworld;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
{%- if cookiecutter[ "Powertools for AWS Lambda (Java) Logging" ] == "enabled" %}
import software.amazon.lambda.powertools.logging.Logging;
{%- endif %}
{%- if cookiecutter[ "Powertools for AWS Lambda (Java) Metrics" ] == "enabled" %}
import software.amazon.lambda.powertools.metrics.Metrics;
{%- endif %}
{%- if cookiecutter[ "Powertools for AWS Lambda (Java) Tracing" ] == "enabled" %}
import software.amazon.lambda.powertools.tracing.Tracing;

import static software.amazon.lambda.powertools.tracing.CaptureMode.*;
{%- endif %}

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    {%- if cookiecutter[ "Powertools for AWS Lambda (Java) Logging" ] == "enabled" %}
    Logger log = LogManager.getLogger(App.class);

    @Logging(logEvent = true)
    {%- endif %}
    {%- if cookiecutter[ "Powertools for AWS Lambda (Java) Tracing" ] == "enabled" %}
    @Tracing(captureMode = DISABLED)
    {%- endif %}
    {%- if cookiecutter[ "Powertools for AWS Lambda (Java) Metrics" ] == "enabled" %}
    @Metrics(captureColdStart = true)
    {%- endif %}
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        var headers = new HashMap<String, String>();
        headers.put("Content-Type", "application/json");
        headers.put("X-Custom-Header", "application/json");

        APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent()
                .withHeaders(headers);
        try {
            final String pageContents = this.getPageContents("https://checkip.amazonaws.com");
            String output = String.format("{ \"message\": \"hello world\", \"location\": \"%s\" }", pageContents);

            return response
                    .withStatusCode(200)
                    .withBody(output);
        } catch (IOException e) {
            return response
                    .withBody("{}")
                    .withStatusCode(500);
        }
    }
    {%- if cookiecutter[ "Powertools for AWS Lambda (Java) Tracing" ] == "enabled" %}
    @Tracing(namespace = "getPageContents")
    {%- endif %}
    private String getPageContents(String address) throws IOException {
        {%- if cookiecutter[ "Powertools for AWS Lambda (Java) Logging" ] == "enabled" %}
        log.info("Retrieving {}", address);
        {%- endif %}
        var url = new URL(address);
        try (BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()))) {
            return br.lines().collect(Collectors.joining(System.lineSeparator()));
        }
    }
}
