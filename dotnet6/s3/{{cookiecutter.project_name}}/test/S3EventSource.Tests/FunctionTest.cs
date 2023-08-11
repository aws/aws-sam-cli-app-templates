using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

using Xunit;
using Moq;
using Amazon.Lambda;
using Amazon.Lambda.Core;
using Amazon.Lambda.TestUtilities;
using Amazon.Lambda.S3Events;

using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using Amazon.S3.Util;

using S3EventSource;

namespace S3EventSource.Tests
{
    public class FunctionTest
    {
        [Fact]
        public async Task TestS3EventLambdaFunction()
        {
            var context = new TestLambdaContext();

            var bucketName = "lambda-S3JsonLogger-".ToLower() + DateTime.Now.Ticks;
            var key = "text.txt";

            // BEGIN mocking s3Client
            var s3ClientMock = new Mock<IAmazonS3>();
            s3ClientMock.Setup(x => x.Config)
                        .Returns(new AmazonS3Config { RegionEndpoint = RegionEndpoint.USWest2 });

            var response = new GetObjectMetadataResponse();
            response.Headers.ContentType = "text/plain";
            response.Expires = DateTime.Now;

            s3ClientMock.Setup(x => x.GetObjectMetadataAsync(
                It.Is<string>(_bucketName => _bucketName == bucketName),    // Mock with the given bucket name
                It.Is<string>(_key => _key == key),                         // Mock with the given key
                It.IsAny<CancellationToken>())
            )
                .Returns(Task.FromResult(response));
        
            var s3Client = s3ClientMock.Object;
            // END mocking s3Client


            // Setup the S3 event object that S3 notifications would create with the fields used by the Lambda function.
            var s3Event = new S3Event
            {
                Records = new List<S3EventNotification.S3EventNotificationRecord>
                {
                    new S3EventNotification.S3EventNotificationRecord
                    {
                        S3 = new S3EventNotification.S3Entity
                        {
                            Bucket = new S3EventNotification.S3BucketEntity { Name = bucketName },
                            Object = new S3EventNotification.S3ObjectEntity { Key = key }
                        }
                    }
                }
            };

            // Invoke the lambda function and confirm the content type was returned.
            var function = new Function(s3Client);
            var contentType = await function.FunctionHandler(s3Event, context);

            Assert.Equal("text/plain", contentType);
        }
    }
}
