exports.handler = awslambda.streamifyResponse(
    async (event, responseStream, context) => {
        const httpResponseMetadata = {
            statusCode: 200,
            headers: {
                "Content-Type": "text/html",
                "X-Custom-Header": "Example-Custom-Header"
            }
        };

        responseStream = awslambda.HttpResponseStream.from(responseStream, httpResponseMetadata);
        // It's recommended to use a `pipeline` over the `write` method for more complex use cases.
        // Learn more: https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html
        responseStream.write("<html>");
        responseStream.write("<p>First write!</p>");

        responseStream.write("<h1>Streaming h1</h1>");
        await new Promise(r => setTimeout(r, 1000));
        responseStream.write("<h2>Streaming h2</h2>");
        await new Promise(r => setTimeout(r, 1000));
        responseStream.write("<h3>Streaming h3</h3>");
        await new Promise(r => setTimeout(r, 1000));
  
        // Long strings will be streamed
        const loremIpsum1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae mi tincidunt tellus ultricies dignissim id et diam. Morbi pharetra eu nisi et finibus. Vivamus diam nulla, vulputate et nisl cursus, pellentesque vehicula libero. Cras imperdiet lorem ante, non posuere dolor sollicitudin a. Vestibulum ipsum lacus, blandit nec augue id, lobortis dictum urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Morbi auctor orci eget tellus aliquam, non maximus massa porta. In diam ante, pulvinar aliquam nisl non, elementum hendrerit sapien. Vestibulum massa nunc, mattis non congue vitae, placerat in quam. Nam vulputate lectus metus, et dignissim erat varius a.";
        responseStream.write(`<p>${loremIpsum1}</p>`);
        await new Promise(r => setTimeout(r, 1000));
  
        responseStream.write("<p>DONE!</p>");
        responseStream.write("</html>");
        responseStream.end();
    }
);
