using Amazon.DynamoDBv2.DataModel;

namespace ServerlessAPI.Entities;

// <summary>
/// Map the Book Class to DynamoDb Table
/// To learn more visit https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DeclarativeTagsList.html
/// </summary>
[DynamoDBTable("{{cookiecutter.project_name}}BookCatalog")]
public class Book
{
    ///<summary>
    /// Map c# types to DynamoDb Columns 
    /// to learn more visit https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/MidLevelAPILimitations.SupportedTypes.html
    /// <summary>
    [DynamoDBHashKey] //Partition key
    public Guid Id { get; set; } = Guid.Empty;

    [DynamoDBProperty]
    public string Title { get; set; } = string.Empty;

    [DynamoDBProperty]
    public string? ISBN { get; set; }

    [DynamoDBProperty] //String Set datatype
    public List<string>? Authors { get; set; }

    [DynamoDBIgnore]
    public string? CoverPage { get; set; }
}
