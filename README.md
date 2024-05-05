## Retrieval-Augmented Generation Assistant API

Welcome to the Retrieval-Augmented Generation Assistant API documentation. This API is designed to provide users with functionalities for retrieving information from URLs and generating responses to user prompts or questions based on the retrieved content.

### Endpoints

#### 1. GET_URL

- **Description**: Fetches content from a given URL (can be html or pdf).
  
- **Method**: `POST`
  
- **Endpoint**: `/get_url`

- **Request Parameters**:
  - `url` (string): The URL from which to retrieve content.

- **Success Responses**:
  - **Code**: `200 OK`
    - **Content**: Null if database was uploaded correctly to InterSystems
    - **Example**:
      The database has been uploaded to the InterSystems website, as indicated in the image provided. 
      ![image](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/132887066/913d99a1-d366-40c7-b6d8-68315a831198)
      Additionally, the API returned null, signifying that the fetched document was found without any issues.
      ![Example Response](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/132887066/6b6e09e8-3a16-468d-902b-7acc14e6a645)

- **Error Responses**:
  - **Code**: `400 Bad Request`
    - **Content**: Raised Error
    - **Example**:
      ![Invalid URL Error](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/132887066/c54a0221-68ce-4f54-88e8-5ca55e479ee2)

#### 2. ASK

- **Description**: Generates a response to a user question based on the content of a specified URL.
  
- **Method**: `POST`
  
- **Endpoint**: `/ask`

- **Request Parameters**:
  - `url` (string): The URL of the content to base the response on.
  - `question` (string): The question posed by the user.

- **Success Responses**:
  - **Code**: `200 OK`
    - **Content**: JSON object containing the generated response.
    - **Example**:
      ```json
      {
        "response": "The response to the user's question...",
        "source_paragraph": "The relevant paragraph from the retrieved content..."
      }
      ```
      ![Example Response](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/132887066/84af8273-60ec-42d6-9293-eaab3e0a8bc8)

- **Error Responses**:
  - **Code**: `400 Bad Request`
    - **Content**: JSON object containing an error message.
    - **Example**:
      ```json
      {
        "error": "Invalid URL provided."
      }
      ```
      ![Invalid URL Error](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/132887066/c54a0221-68ce-4f54-88e8-5ca55e479ee2)

### Usage

To use the Retrieval-Augmented Generation Assistant API, make HTTP POST requests to the appropriate endpoints with the required parameters.

### Example

Here's an example of how to use the API with cURL:

```bash
curl -X POST \
  https://example.com/api/v1/get_url \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com"
  }'
```

### Notes

- Ensure that the URLs provided are accessible and contain valid content.
- The API may return errors for invalid or inaccessible URLs.
