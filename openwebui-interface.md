Endpoint

  POST /api/v1/files/

  Request

  - Content-Type: multipart/form-data
  - Auth: Authorization: Bearer <API_KEY>
  - Body: file binary under the file form field

  curl -X POST \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -F "file=@/path/to/document.pdf" \
    http://localhost:3000/api/v1/files/

  Response

  Returns file metadata immediately — processing happens async in the background:
  {
    "id": "unique_file_id",
    "filename": "document.pdf",
    "size": 1024000,
    "mimetype": "application/pdf",
    "hash": "file_content_hash",
    "user_id": "...",
    "created_at": "..."
  }

  Key details

  - Processing (content extraction + embeddings) runs asynchronously by default
  - Optional query params: process=true (default) and process_in_background=true
  - You can check status via GET /api/v1/files/{id}/process/status