package helloworld;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import {{ cookiecutter.AWS_Schema_root }}.AWSEvent;
import {{ cookiecutter.AWS_Schema_root }}.{{ cookiecutter.AWS_Schema_name }};
import {{ cookiecutter.AWS_Schema_root }}.marshaller.Marshaller;

/**
 * Handler for EventBridge invocations of a Lambda function target
 */
public class App implements RequestStreamHandler {

    static final String NEW_DETAIL_TYPE = "{{ cookiecutter.function_name }} updated event of %s";

    private Object handleEvent(final AWSEvent<{{ cookiecutter.AWS_Schema_name }}> inputEvent, final Context context) {
	    if (inputEvent != null) {
            {{ cookiecutter.AWS_Schema_name }} detail = inputEvent.getDetail();

            //Developers write your event-driven business logic code here, such as...
            inputEvent.setDetailType(String.format(NEW_DETAIL_TYPE, inputEvent.getDetailType()));

            return inputEvent;
        }

        throw new IllegalArgumentException("Unable to deserialize lambda input event to AWSEvent<{{ cookiecutter.AWS_Schema_name }}>. Check that you have the right schema and event source.");
    }

    /**
     * Handles a Lambda Function request
     * @param input The Lambda Function input stream
     * @param output The Lambda function output stream
     * @param context The Lambda execution environment context object.
     * @throws IOException
     */
    public void handleRequest(InputStream input, OutputStream output, Context context) throws IOException {
        AWSEvent<{{ cookiecutter.AWS_Schema_name }}> event = Marshaller.unmarshalEvent(input, {{ cookiecutter.AWS_Schema_name }}.class);

        Object response = handleEvent(event, context);

        Marshaller.marshal(output, response);
    }
}
