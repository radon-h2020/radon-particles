## ServerlessToDoListAPI Blueprint

This blueprint represents a serverless API for managing a list of TODO items implemented using Amazon Web Services (AWS Lambda, AWS API Gateway, AWS DynamoDB).
The functions are implemented in node.js based on <https://github.com/kraigh/serverless-todo-api>.

## API Specification

The ToDo API Consists of the following functions:

- `POST /todos`: Create a ToDo Item
- `GET /todos`: List all ToDo items
- `GET /todos/{id}`: Get a specific ToDo item
- `PUT /todos/{id}`: Update a ToDo Item
- `DELETE /todos/{id}`: Delete a ToDo Item

All Methods produce JSON responses and accept JSON requests.

### ToDo Item

```json
{
  "id": "8c299858-4bf0-4b2d-89ea-36bd5dc09fde",
  "todo": "Have a coffee :-)",
  "completed": false,
  "created": 1566323969,
  "updated": 1566323995
}
```

- `id`: ID of the inserted element. This does not have to be a Guid
- `todo`: ToDo Item to insert
- `completed`: Item's completion status
- `created`: Task creation timestamp
- `updated`: Task update timestamp

### ItemCreation Request

```json
{
  "todo": "Have one more coffee :-)"
}
```

- `todo`: The ToDo Item to insert (Required)
