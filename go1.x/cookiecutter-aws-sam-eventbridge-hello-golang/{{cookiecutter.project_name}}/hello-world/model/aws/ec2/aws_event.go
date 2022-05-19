package ec2

import (
    "time"
)

type AWSEvent struct {
    Detail EC2InstanceStateChangeNotification `json:"detail"`
    DetailType string   `json:"detail-type"`
    Resources []string `json:"resources"`
    Id     string    `json:"id"`
    Source string    `json:"source"`
    Time    time.Time `json:"time"`
    Region  string `json:"region"`
    Version string `json:"version"`
    Account string `json:"account"`
}

func (a *AWSEvent) SetDetail(detail EC2InstanceStateChangeNotification) {
    a.Detail = detail
}

func (a *AWSEvent) SetDetailType(detailType string) {
    a.DetailType = detailType
}

func (a *AWSEvent) SetResources(resources []string) {
    a.Resources = resources
}

func (a *AWSEvent) SetId(id string) {
    a.Id = id
}

func (a *AWSEvent) SetSource(source string) {
    a.Source = source
}

func (a *AWSEvent) SetTime(time time.Time) {
    a.Time = time
}

func (a *AWSEvent) SetRegion(region string) {
    a.Region = region
}

func (a *AWSEvent) SetVersion(version string) {
    a.Version = version
}

func (a *AWSEvent) SetAccount(account string) {
    a.Account = account
}
