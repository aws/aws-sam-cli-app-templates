package main

import (
	"context"
	"testing"
)

func TestHandler(t *testing.T) {
	t.Run("Check response properties", func(t *testing.T) {
		context := context.Background()
		response, _ := handler(context)

		if (response.StockPrice < 0 || response.StockPrice > 99) {
			t.Fatal("Response has invalid field value")
		}
	})
}
