package main

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"io/ioutil"
	"os"
	"testing"
	"{{ cookiecutter.project_name }}/hello-world/model/aws/ec2/marshaller"
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

	awsEvent, _ := marshaller.UnmarshalEvent(jsonStream)

	t.Run("Successful Request", func(t *testing.T) {
		responseStream, err := handler(nil, awsEvent)
		if err != nil {
			t.Fatal("Everything should be ok")
		}

		responseEvent, _  := marshaller.UnmarshalEvent(responseStream)
		responseEc2Notification := responseEvent.Detail

		assert.NotEmpty(t, responseEvent)
		assert.Equal(t, responseEvent.DetailType, "HelloWorldFunction updated event of EC2 Instance State-change Notification")
		assert.Equal(t, responseEc2Notification.InstanceId, "i-abcd1111")
	})
}
