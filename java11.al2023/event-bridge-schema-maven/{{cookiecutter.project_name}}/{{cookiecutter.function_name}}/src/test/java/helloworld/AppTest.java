package helloworld;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;

import org.junit.Ignore;
import org.junit.Test;

import helloworld.App;
import {{ cookiecutter.AWS_Schema_root }}.AWSEvent;
import {{ cookiecutter.AWS_Schema_root }}.{{ cookiecutter.AWS_Schema_name }};
import {{ cookiecutter.AWS_Schema_root }}.marshaller.Marshaller;

public class AppTest {
    @Test
    public void successfulResponse() throws IOException {
        App app = new App();

        {{ cookiecutter.AWS_Schema_name }} detail = new {{ cookiecutter.AWS_Schema_name }}();

        AWSEvent<{{ cookiecutter.AWS_Schema_name }}> event =
                new AWSEvent<{{ cookiecutter.AWS_Schema_name }}>()
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

