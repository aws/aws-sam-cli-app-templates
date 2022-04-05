package marshaller

import (
    "encoding/json"
    "{{ cookiecutter.project_name }}/hello-world/model/aws/ec2"
)

func Marshal(inputEvent interface{}) ([]byte, error) {
    outputStream, err := json.Marshal(inputEvent)
    if err != nil {
        return nil, err
    }

    return outputStream, nil
}

func Unmarshal(inputStream []byte) (map[string]interface{}, error) {
    var outputEvent map[string]interface{}
    err := json.Unmarshal(inputStream, &outputEvent)
    if err != nil {
        return nil, err
    }

    return outputEvent, nil
}

func UnmarshalEvent(inputStream []byte) (ec2.AWSEvent, error) {
    var outputEvent ec2.AWSEvent
    err := json.Unmarshal(inputStream, &outputEvent)
    if err != nil {
        return ec2.AWSEvent{}, err
    }

    return outputEvent, nil
}
