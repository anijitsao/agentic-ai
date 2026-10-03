from pydantic import BaseModel


class ChatRequestModel(BaseModel):
    prompt: str = "describe python"


class ChatResponse(BaseModel):
    prompt: str
    response: str


class ChatResponseModel(BaseModel):
    data: ChatResponse
