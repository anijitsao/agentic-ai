from pydantic import BaseModel


class ChatResponse(BaseModel):
    prompt: str
    response: str


class ChatResponseModel(BaseModel):
    data: ChatResponse
