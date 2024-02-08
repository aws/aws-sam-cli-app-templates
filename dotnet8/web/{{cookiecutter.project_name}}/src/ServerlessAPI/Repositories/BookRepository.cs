using Amazon.DynamoDBv2.DataModel;
using Amazon.DynamoDBv2.DocumentModel;
using ServerlessAPI.Entities;

namespace ServerlessAPI.Repositories;

public class BookRepository : IBookRepository
{
    private readonly IDynamoDBContext context;
    private readonly ILogger<BookRepository> logger;

    public BookRepository(IDynamoDBContext context, ILogger<BookRepository> logger)
    {
        this.context = context;
        this.logger = logger;
    }

    public async Task<bool> CreateAsync(Book book)
    {
        try
        {
            book.Id = Guid.NewGuid();
            await context.SaveAsync(book);
            logger.LogInformation("Book {} is added", book.Id);
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "fail to persist to DynamoDb Table");
            return false;
        }

        return true;
    }

    public async Task<bool> DeleteAsync(Book book)
    {
        bool result;
        try
        {
            // Delete the book.
            await context.DeleteAsync<Book>(book.Id);
            // Try to retrieve deleted book. It should return null.
            Book deletedBook = await context.LoadAsync<Book>(book.Id, new DynamoDBContextConfig
            {
                ConsistentRead = true
            });

            result = deletedBook == null;
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "fail to delete book from DynamoDb Table");
            result = false;
        }

        if (result) logger.LogInformation("Book {Id} is deleted", book);

        return result;
    }

    public async Task<bool> UpdateAsync(Book book)
    {
        if (book == null) return false;

        try
        {
            await context.SaveAsync(book);
            logger.LogInformation("Book {Id} is updated", book);
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "fail to update book from DynamoDb Table");
            return false;
        }

        return true;
    }

    public async Task<Book?> GetByIdAsync(Guid id)
    {
        try
        {
            return await context.LoadAsync<Book>(id);
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "fail to update book from DynamoDb Table");
            return null;
        }
    }

    public async Task<IList<Book>> GetBooksAsync(int limit = 10)
    {
        var result = new List<Book>();

        try
        {
            if (limit <= 0)
            {
                return result;
            }

            var filter = new ScanFilter();
            filter.AddCondition("Id", ScanOperator.IsNotNull);
            var scanConfig = new ScanOperationConfig()
            {
                Limit = limit,
                Filter = filter
            };
            var queryResult = context.FromScanAsync<Book>(scanConfig);

            do
            {
                result.AddRange(await queryResult.GetNextSetAsync());
            }
            while (!queryResult.IsDone && result.Count < limit);
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "fail to list books from DynamoDb Table");
            return new List<Book>();
        }

        return result;
    }
}