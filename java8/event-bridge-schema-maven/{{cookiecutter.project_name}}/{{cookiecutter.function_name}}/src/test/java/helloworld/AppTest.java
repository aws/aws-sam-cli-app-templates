package helloworld;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;

import org.junit.Test;

import {{ cookiecutter.AWS_Schema_root }}.AWSEvent;
import {{ cookiecutter.AWS_Schema_root }}.{{ cookiecutter.AWS_Schema_name }};
import {{ cookiecutter.AWS_Schema_root }}.marshaller.Marshaller;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

public class AppTest {

    private static final String MY_DETAIL_TYPE = "myDetailType";

    @Test
    public void successfulResponse() throws IOException {
        AWSEvent<{{ cookiecutter.AWS_Schema_name }}> event =
                new AWSEvent<{{ cookiecutter.AWS_Schema_name }}>()
                .detail(new {{ cookiecutter.AWS_Schema_name }}())
                        .detailType(MY_DETAIL_TYPE);

        ByteArrayOutputStream handlerOutput = new ByteArrayOutputStream();

        App app = new App();
        app.handleRequest(toInputStream(event), handlerOutput, null);

        AWSEvent<{{ cookiecutter.AWS_Schema_name }}> responseEvent = fromOutputStream(handlerOutput);
        assertNotNull(responseEvent);
        assertEquals(String.format(App.NEW_DETAIL_TYPE, MY_DETAIL_TYPE), responseEvent.getDetailType());
    }

    private InputStream toInputStream(AWSEvent<{{ cookiecutter.AWS_Schema_name }}> event) throws IOException {
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        Marshaller.marshal(output, event);

        return new ByteArrayInputStream(output.toByteArray());
    }

    private AWSEvent<{{ cookiecutter.AWS_Schema_name }}> fromOutputStream(ByteArrayOutputStream outputStream) throws IOException {
        ByteArrayInputStream inputStream = new ByteArrayInputStream(outputStream.toByteArray());

        return Marshaller.unmarshalEvent(inputStream, {{ cookiecutter.AWS_Schema_name }}.class);
    }
}

