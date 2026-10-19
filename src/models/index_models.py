from pydantic import BaseModel


class IndexResponse(BaseModel):
    message: str

class IndexResponseModel(BaseModel):
    data: IndexResponse
