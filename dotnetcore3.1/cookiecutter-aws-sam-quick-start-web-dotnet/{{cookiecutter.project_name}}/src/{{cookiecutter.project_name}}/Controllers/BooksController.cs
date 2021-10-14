using System;
using System.Collections.Generic;
using System.Threading.Tasks;

using Microsoft.AspNetCore.Mvc;

using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;
using Amazon.Lambda.Core;

using {{cookiecutter.project_name}}.Entities;
using Amazon.DynamoDBv2.DocumentModel;

namespace {{cookiecutter.project_name}}.Controllers
{
    [Route("api/[controller]")]
    public class BooksController : ControllerBase
    {
        private readonly IAmazonDynamoDB client;
        private readonly DynamoDBContext context;

        public BooksController(IAmazonDynamoDB client)
        {
            this.client = client;
            this.context = new DynamoDBContext(client);
        }

        // GET api/books
        [HttpGet]
        public async Task<IEnumerable<Book>> Get()
        {
            var result = new List<Book>();

            ScanFilter filter = new ScanFilter();
            filter.AddCondition("Title", ScanOperator.IsNotNull);
            ScanOperationConfig scanConfig = new ScanOperationConfig
            {
                Limit = 10,
                Filter = filter
            };
            var queryResult = context.FromScanAsync<Book>(scanConfig);

            do
            {
                result.AddRange(await queryResult.GetNextSetAsync());
            }
            while (!queryResult.IsDone && result.Count < 10);

            return result;
        }

        // GET api/books/5
        [HttpGet("{id}")]
        public async Task<Book> Get(Guid id)
        {
            LambdaLogger.Log($"Looking for book {id}");
            return await context.LoadAsync<Book>(id);
        }

        // POST api/books
        [HttpPost]
        public async Task Post([FromBody] Book book)
        {
            if (book == null )
            {
                throw new ArgumentException("Invalid input! Book not informed");
            }

            await context.SaveAsync<Book>(book);
            LambdaLogger.Log($"Book {book.Id} is added");
        }

        // PUT api/books/5
        [HttpPut("{id}")]
        public async Task Put(Guid id, [FromBody] Book book)
        {
            // Retrieve the book.
            Book bookRetrieved = await context.LoadAsync<Book>(id);

            if (bookRetrieved == null)
            {
                var errorMsg = $"Invalid input! No book found with id:{id}";
                LambdaLogger.Log(errorMsg);
                throw new ArgumentException(errorMsg);
            }

            book.Id = bookRetrieved.Id;

            await context.SaveAsync<Book>(book);
            LambdaLogger.Log($"Book {book.Id} is updated");
        }

        // DELETE api/books/5
        [HttpDelete("{id}")]
        public async Task Delete(Guid id)
        {
            // Delete the book.
            await context.DeleteAsync<Book>(id);
            // Try to retrieve deleted book. It should return null.
            Book deletedBook = await context.LoadAsync<Book>(id, new DynamoDBContextConfig
            {
                ConsistentRead = true
            });

            if (deletedBook == null)
                LambdaLogger.Log($"Book {id} is deleted");
        }
    }
}
