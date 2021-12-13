use lambda_http::{
    handler,
    lambda_runtime::{self, Context, Error},
    IntoResponse, Request, Response,
};

#[tokio::main]
async fn main() -> Result<(), Error> {
    lambda_runtime::run(handler(hello)).await?;

    Ok(())
}

/// Sample pure Lambda function
async fn hello(_request: Request, _context: Context) -> Result<impl IntoResponse, Error> {
    Ok(Response::builder()
        .status(200)
        .header("Content-Type", "text/plain")
        .body("Hello, World!".to_string())?)
}

#[tokio::test]
async fn test_hello() {
    let request = Request::default();
    let response = hello(request, Context::default())
        .await
        .unwrap()
        .into_response();
    assert_eq!(
        response.body(),
        &lambda_http::Body::Text("Hello, World!".to_string())
    );
}
