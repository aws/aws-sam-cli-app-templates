package helloworld;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import org.junit.Test;

import model.aws.ec2.AWSEvent;
import model.aws.ec2.EC2InstanceStateChangeNotification;
import model.aws.ec2.marshaller.Marshaller;

public class AppTest {
    @Test
    public void successfulResponse() throws IOException {
        App app = new App();

        EC2InstanceStateChangeNotification detail = new EC2InstanceStateChangeNotification();

        AWSEvent<EC2InstanceStateChangeNotification> event =
                new AWSEvent<EC2InstanceStateChangeNotification>()
                        .detail(detail);

        InputStream handlerInput = toInputStream(event);
        OutputStream handlerOutput = testStringOutputStream();

        app.handleRequest(handlerInput, handlerOutput, null);
    }

    private InputStream toInputStream(AWSEvent event) throws IOException {
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        Marshaller.marshal(output, event);

        return new ByteArrayInputStream(output.toByteArray());
    }

    private OutputStream testStringOutputStream() {
        return new OutputStream() {
            private StringBuilder string = new StringBuilder();

            @Override
            public void write(int x) throws IOException {
                this.string.append((char) x);
            }

            public String toString() {
                return this.string.toString();
            }
        };
    }
}

