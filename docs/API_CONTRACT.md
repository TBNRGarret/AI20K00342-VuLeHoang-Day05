# API Contract

## Chat Endpoint

**URL**: `/chat`
**Method**: `POST`
**Body**:
```json
{
  "message": "string"
}
```

**Outcome**:
- **200 OK**:
```json
{
  "reply": "string",
  "sources": ["string"]
}
```
- **422 Unprocessable Entity**: Lỗi định dạng dữ liệu đầu vào.
