using Amazon.DynamoDBv2.DataModel;
using Microsoft.AspNetCore.Mvc;
using ServerlessAPI.Entities;
using ServerlessAPI.Repositories;

namespace ServerlessAPI.Controllers;

[Route("api/[controller]")]
[Produces("application/json")]
public class BooksController : ControllerBase
{
    private readonly ILogger<BooksController> logger;
    private readonly IBookRepository bookRepository;

    public BooksController(ILogger<BooksController> logger, IBookRepository bookRepository)
    {
        this.logger = logger;
        this.bookRepository = bookRepository;
    }

    // GET api/books
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Book>>> Get([FromQuery] int limit = 10)
    {
        if (limit <= 0 || limit > 100) return BadRequest("The limit should been between [1-100]");

        return Ok(await bookRepository.GetBooksAsync(limit));
    }

    // GET api/books/5
    [HttpGet("{id}")]
    public async Task<ActionResult<Book>> Get(Guid id)
    {
        var result = await bookRepository.GetByIdAsync(id);

        if (result == null)
        {
            return NotFound();
        }

        return Ok(result);
    }

    // POST api/books
    [HttpPost]
    public async Task<ActionResult<Book>> Post([FromBody] Book book)
    {
        if (book == null) return ValidationProblem("Invalid input! Book not informed");

        var result = await bookRepository.CreateAsync(book);

        if (result)
        {
            return CreatedAtAction(
                nameof(Get),
                new { id = book.Id },
                book);
        }
        else
        {
            return BadRequest("Fail to persist");
        }

    }

    // PUT api/books/5
    [HttpPut("{id}")]
    public async Task<IActionResult> Put(Guid id, [FromBody] Book book)
    {
        if (id == Guid.Empty || book == null) return ValidationProblem("Invalid request payload");

        // Retrieve the book.
        var bookRetrieved = await bookRepository.GetByIdAsync(id);

        if (bookRetrieved == null)
        {
            var errorMsg = $"Invalid input! No book found with id:{id}";
            return NotFound(errorMsg);
        }

        book.Id = bookRetrieved.Id;

        await bookRepository.UpdateAsync(book);
        return Ok();
    }

    // DELETE api/books/5
    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete(Guid id)
    {
        if (id == Guid.Empty) return ValidationProblem("Invalid request payload");

        var bookRetrieved = await bookRepository.GetByIdAsync(id);

        if (bookRetrieved == null)
        {
            var errorMsg = $"Invalid input! No book found with id:{id}";
            return NotFound(errorMsg);
        }

        await bookRepository.DeleteAsync(bookRetrieved);
        return Ok();
    }
}
