use aws_sdk_dynamodb::{model::AttributeValue, Client};
use lambda_http::{
    ext::RequestExt,
    handler,
    lambda_runtime::{self, Context, Error},
    Body, IntoResponse, Request, Response,
};
use std::env;

#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = aws_config::load_from_env().await;
    let table_name = env::var("TABLE_NAME").expect("TABLE_NAME must be set");
    let dynamodb_client = Client::new(&config);

    lambda_runtime::run(handler(|request: Request, context: Context| {
        put_item(&dynamodb_client, &table_name, request, context)
    }))
    .await?;

    Ok(())
}

async fn put_item<C>(
    client: &Client<C>,
    table_name: &str,
    request: Request,
    _context: Context,
) -> Result<impl IntoResponse, Error>
where
    C: aws_smithy_client::bounds::SmithyConnector,
{
    // Extract path parameter from request
    let path_parameters = request.path_parameters();
    let id = match path_parameters.get("id") {
        Some(id) => id,
        None => return Ok(Response::builder().status(400).body("id is required")?),
    };

    // Extract body from request
    let body = match request.body() {
        Body::Empty => "".to_string(),
        Body::Text(body) => body.clone(),
        Body::Binary(body) => String::from_utf8_lossy(body).to_string(),
    };

    // Put the item in the DynamoDB table
    let res = client
        .put_item()
        .table_name(table_name)
        .item("id", AttributeValue::S(id.to_string()))
        .item("payload", AttributeValue::S(body))
        .send()
        .await;

    // Return a response to the end-user
    match res {
        Ok(_) => Ok(Response::builder().status(200).body("item saved")?),
        Err(_) => Ok(Response::builder().status(500).body("internal error")?),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use aws_sdk_dynamodb::{Client, Config, Credentials, Region};
    use aws_smithy_client::test_connection::TestConnection;
    use aws_smithy_http::body::SdkBody;
    use std::collections::HashMap;

    async fn get_mock_config() -> Config {
        let cfg = aws_config::from_env()
            .region(Region::new("eu-west-1"))
            .credentials_provider(Credentials::from_keys("access_key", "privatekey", None))
            .load()
            .await;

        Config::new(&cfg)
    }

    fn get_request_builder() -> http::request::Builder {
        http::Request::builder()
            .header("content-type", "application/x-amz-json-1.0")
            .uri(http::uri::Uri::from_static(
                "https://dynamodb.eu-west-1.amazonaws.com/",
            ))
    }

    #[tokio::test]
    async fn test_put_item() {
        // Mock DynamoDB client
        let conn = TestConnection::new(vec![(
            get_request_builder()
                .header("x-amz-target", "DynamoDB_20120810.PutItem")
                .body(SdkBody::from(
                    r#"{"TableName":"test","Item":{"id":{"S":"1"},"payload":{"S":"test1"}}}"#,
                ))
                .unwrap(),
            http::Response::builder()
                .status(200)
                .body(SdkBody::from(
                    r#"{"Attributes": {"id": {"S": "1"}, "payload": {"S": "test1"}}}"#,
                ))
                .unwrap(),
        )]);
        let client = Client::from_conf_conn(get_mock_config().await, conn.clone());

        let table_name = "test_table";

        // Mock API Gateway request
        let mut path_parameters = HashMap::new();
        path_parameters.insert("id".to_string(), vec!["1".to_string()]);

        let request = http::Request::builder()
            .method("PUT")
            .uri("/1")
            .body(Body::Text("test1".to_string()))
            .unwrap()
            .with_path_parameters(path_parameters);

        // Send mock request to Lambda handler function
        let response = put_item(&client, table_name, request, Context::default())
            .await
            .unwrap()
            .into_response();

        // Assert that the response is correct
        assert_eq!(response.status(), 200);
        assert_eq!(response.body(), &Body::Text("item saved".to_string()));
    }
}
