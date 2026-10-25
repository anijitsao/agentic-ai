from pydantic import BaseModel


class IntentCheck(BaseModel):
    is_information_related: bool
    reasoning: str
