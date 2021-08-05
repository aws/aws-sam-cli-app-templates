extern crate jemallocator;

#[global_allocator]
static ALLOC: jemallocator::Jemalloc = jemallocator::Jemalloc;

use bytes::Bytes;
use lambda_runtime::{ handler_fn, Context, Error };
use serde_json::{ json, Value };

use aws_sdk_s3 as s3;
use s3::Region;

use tracing_subscriber::fmt::format::FmtSpan;
use tracing_subscriber::fmt::SubscriberBuilder;

// Change these to your bucket, key and region
const BUCKET: &str = "samlocal";
const KEY: &str = "testobject.txt";
const REGION: &str = "ap-southeast-2";


#[tokio::main]
async fn main() -> Result<(), Error> {
    lambda_runtime::run(handler_fn(read_s3_object)).await?;
    Ok(())
}

async fn read_s3_object(_event: Value, _ctx: Context) -> Result<Value, Error> {
    let s3_object = stream_s3_object().await?;
    dbg!(&s3_object);
    Ok(json!({ "message": &*s3_object }))
}

/// Fetches S3 object
async fn stream_s3_object() -> Result<Bytes, Error> {
    SubscriberBuilder::default()
        .with_env_filter("info")
        .with_span_events(FmtSpan::CLOSE)
        .init();
    let conf = s3::Config::builder()
        .region(Region::new(REGION))
        .build();
    let client = s3::Client::from_conf(conf);

    let resp = client.get_object().bucket(BUCKET).key(KEY).send().await?;
    let data = resp.body.collect().await?;

    return Ok(data.into_bytes());
}
