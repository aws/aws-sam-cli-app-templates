package main

import (
	"fmt"
	"io"
	"net/http"
	"time"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

const (
	loreIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae mi tincidunt tellus ultricies dignissim id et diam. Morbi pharetra eu nisi et finibus. Vivamus diam nulla, vulputate et nisl cursus, pellentesque vehicula libero. Cras imperdiet lorem ante, non posuere dolor sollicitudin a. Vestibulum ipsum lacus, blandit nec augue id, lobortis dictum urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Morbi auctor orci eget tellus aliquam, non maximus massa porta. In diam ante, pulvinar aliquam nisl non, elementum hendrerit sapien. Vestibulum massa nunc, mattis non congue vitae, placerat in quam. Nam vulputate lectus metus, et dignissim erat varius a."
)

func renderPage(sleep func(time.Duration), w io.Writer) {
	fmt.Fprintln(w, "<!DOCTYPE html>")
	fmt.Fprintln(w, "<html><head><title>Hello ƛ</title></head><body>")
	fmt.Fprintln(w, "<p>First Write!</p>")
	for i := 1; i <= 3; i++ {
		fmt.Fprintf(w, "<h%d>Streaming h%d</h%d>\n", i, i, i)
		sleep(time.Second)
	}
	fmt.Fprintf(w, "<p>%s</p>\n", loreIpsum)
	sleep(time.Second)
	fmt.Fprintln(w, "<p>DONE!</p>")
	fmt.Fprintln(w, "</body></html>")
}

func lambdaHandler(request *events.LambdaFunctionURLRequest) (*events.LambdaFunctionURLStreamingResponse, error) {
	r, w := io.Pipe()
	go func() {
		defer w.Close()
		renderPage(time.Sleep, w)
	}()
	return &events.LambdaFunctionURLStreamingResponse{
		StatusCode: http.StatusOK,
		Headers: map[string]string{
			"Content-Type":    "text/html; charset=utf-8",
			"X-Custom-Header": "Example-Custom-Header",
		},
		Body: r,
	}, nil
}

func main() {
	lambda.Start(lambdaHandler)
}
