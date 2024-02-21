using ServerlessAPI.Entities;

namespace ServerlessAPI.Repositories;

/// <summary>
/// Sample DynamoDB Table book CRUD
/// </summary>
public interface IBookRepository
{
    /// <summary>
    /// Include new book to the DynamoDB Table
    /// </summary>
    /// <param name="book">book to include</param>
    /// <returns>success/failure</returns>
    Task<bool> CreateAsync(Book book);
    
    /// <summary>
    /// Remove existing book from DynamoDB Table
    /// </summary>
    /// <param name="book">book to remove</param>
    /// <returns></returns>
    Task<bool> DeleteAsync(Book book);

    /// <summary>
    /// List book from DynamoDb Table with items limit (default=10)
    /// </summary>
    /// <param name="limit">limit (default=10)</param>
    /// <returns>Collection of books</returns>
    Task<IList<Book>> GetBooksAsync(int limit = 10);

    /// <summary>
    /// Get book by PK
    /// </summary>
    /// <param name="id">book`s PK</param>
    /// <returns>Book object</returns>
    Task<Book?> GetByIdAsync(Guid id);
    
    /// <summary>
    /// Update book content
    /// </summary>
    /// <param name="book">book to be updated</param>
    /// <returns></returns>
    Task<bool> UpdateAsync(Book book);
}