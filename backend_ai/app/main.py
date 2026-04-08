from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Chatbot Tài Xế Xanh SM API")

class ChatQuery(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str
    sources: List[str] = []

@app.get("/")
async def root():
    return {"message": "Welcome to Chatbot Tài Xế Xanh SM API"}

@app.post("/chat", response_model=ChatResponse)
async def chat(query: ChatQuery):
    # DUMMY RESPONSE - To be implemented with RAG logic
    return {
        "reply": f"Xin chào! Tôi đã nhận được tin nhắn: '{query.message}'. Hệ thống RAG đang được phát triển.",
        "sources": ["readme.md"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
