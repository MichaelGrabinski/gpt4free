from fastapi import FastAPI
from pydantic import BaseModel
import g4f

app = FastAPI()

class ChatRequest(BaseModel):
    messages: list[dict]

@app.post("/v1/chat/completions")
async def chat(req: ChatRequest):
    reply = await g4f.ChatCompletion.create_async(
        model="gpt-4o",
        messages=req.messages
    )
    return {"choices": [{"message": {"content": reply}}]}
