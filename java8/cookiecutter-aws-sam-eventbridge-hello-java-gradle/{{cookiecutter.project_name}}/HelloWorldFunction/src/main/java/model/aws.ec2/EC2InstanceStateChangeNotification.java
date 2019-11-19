package model.aws.ec2;

import java.io.Serializable;
import java.util.Objects;

import com.fasterxml.jackson.annotation.JsonProperty;

public class EC2InstanceStateChangeNotification implements Serializable {
  private static final long serialVersionUID = 1L;

    @JsonProperty("instance-id")
    private String instanceId = null;

    @JsonProperty("state")
    private String state = null;

    public EC2InstanceStateChangeNotification instanceId(String instanceId) {
        this.instanceId = instanceId;
        return this;
    }


    public String getInstanceId() {
        return instanceId;
    }

    public void setInstanceId(String instanceId) {
        this.instanceId = instanceId;
    }

    public EC2InstanceStateChangeNotification state(String state) {
        this.state = state;
        return this;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        EC2InstanceStateChangeNotification ec2InstanceStateChangeNotification = (EC2InstanceStateChangeNotification) o;
        return Objects.equals(this.instanceId, ec2InstanceStateChangeNotification.instanceId) &&
                Objects.equals(this.state, ec2InstanceStateChangeNotification.state);
    }

    @Override
    public int hashCode() {
        return java.util.Objects.hash(instanceId, state);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class EC2InstanceStateChangeNotification {\n");

        sb.append("    instanceId: ").append(toIndentedString(instanceId)).append("\n");
        sb.append("    state: ").append(toIndentedString(state)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
