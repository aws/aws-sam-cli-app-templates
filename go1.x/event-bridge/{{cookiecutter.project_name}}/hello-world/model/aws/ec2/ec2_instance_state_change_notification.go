package ec2

type EC2InstanceStateChangeNotification struct {
    InstanceId string `json:"instance-id"`
    State      string `json:"state"`
}

func (e *EC2InstanceStateChangeNotification) SetInstanceId(instanceId string) {
    e.InstanceId = instanceId
}

func (e *EC2InstanceStateChangeNotification) SetState(state string) {
    e.State = state
}
