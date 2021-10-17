using System;
using System.Collections.Generic;
using Amazon.DynamoDBv2.DataModel;


namespace {{cookiecutter.project_name}}.Entities
{

    /// <summary>
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
        public Guid Id { get; set; }

        [DynamoDBProperty]
        public string Title { get; set; }

        [DynamoDBProperty]
        public int ISBN { get; set; }

        [DynamoDBProperty("Authors")] //String Set datatype
        public List<string> BookAuthors { get; set; }

        [DynamoDBIgnore]
        public string CoverPage { get; set; }
    }
}
