package main

import (
	"context"
	"strconv"
	"testing"
)

func TestHandler(t *testing.T) {
	t.Run("Check response properties", func(t *testing.T) {
		event := StockEvent{StockPrice: 75}
		context := context.Background()
		response, _ := handler(context, event)

		_, idOk := interface{}(response.Id).(string)
		price, priceOk := interface{}(response.Price).(string)
		respType, typeOk := interface{}(response.TransactionType).(string)
		_, qtyOk := interface{}(response.Qty).(string)
		_, timestampOk := interface{}(response.Timestamp).(string)

		if(!idOk || !priceOk || !typeOk || !qtyOk || !timestampOk) {
			t.Fatal("Response missing property")
		}

		if(respType != "buy" || price != strconv.FormatInt(int64(event.StockPrice), 10)) {
			t.Fatal("Response invalid property value")
		}
	})
}
