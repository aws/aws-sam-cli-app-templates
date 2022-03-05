using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;
using Amazon.DynamoDBv2.DocumentModel;
using Microsoft.AspNetCore.Mvc;
using {{cookiecutter.project_name}}.Entities;

namespace {{cookiecutter.project_name}}.Controllers;

[Route("api/[controller]")]
public class BooksController : ControllerBase
{
    private readonly ILogger<BooksController> _logger;

    private readonly IAmazonDynamoDB client;
    private readonly DynamoDBContext context;

    public BooksController(IAmazonDynamoDB client, ILogger<BooksController> logger)
    {
        this.client = client;
        this.context = new DynamoDBContext(client);
        this._logger = logger;
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
        _logger.LogInformation($"Looking for book {id}");
        return await context.LoadAsync<Book>(id);
    }

    // POST api/books
    [HttpPost]
    public async Task Post([FromBody] Book book)
    {
        
        if (book == null)
        {
            throw new ArgumentException("Invalid input! Book not informed");
        }

        await context.SaveAsync<Book>(book);
        _logger.LogInformation($"Book {book.Id} is added");
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
            _logger.LogInformation(errorMsg);
            throw new ArgumentException(errorMsg);
        }

        book.Id = bookRetrieved.Id;

        await context.SaveAsync<Book>(book);
        _logger.LogInformation($"Book {book.Id} is updated");
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
            _logger.LogInformation($"Book {id} is deleted");
    }
}
