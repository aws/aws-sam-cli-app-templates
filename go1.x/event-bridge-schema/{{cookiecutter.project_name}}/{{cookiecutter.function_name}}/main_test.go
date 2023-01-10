package main

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"io/ioutil"
	"os"
	"testing"
	"{{ cookiecutter.codegen_path }}"
)

var (
	PathToEventJsonFile = "../events/event.json"
)

func TestHandler(t *testing.T) {
	jsonFile, err := os.Open(PathToEventJsonFile)
	if err != nil {
		t.Fatal("Unable to open event.json")
	}

	fmt.Println("Successfully Opened event.json")

	defer jsonFile.Close()

	jsonStream, _ := ioutil.ReadAll(jsonFile)

	event, _ := {{ cookiecutter.codegen_package_name }}.UnmarshalEvent(jsonStream)

	t.Run("Successful Request", func(t *testing.T) {
		responseStream, err := handler(nil, event)
		if err != nil {
			t.Fatal("Everything should be ok")
		}

		responseEvent, _  := {{ cookiecutter.codegen_package_name }}.UnmarshalEvent(responseStream)

		assert.NotEmpty(t, responseEvent)
		assert.Equal(t, responseEvent.DetailType, "{{cookiecutter.function_name}} updated event of {{ cookiecutter.AWS_Schema_detail_type }}")
	})
}
