from pydantic import BaseModel, Field


class ChatRequestModel(BaseModel):
    prompt: str = "describe python"


class ChatResponse(BaseModel):
    prompt: str
    response: str


class ChatResponseModel(BaseModel):
    prompt: str = Field(
        description="The original user prompt or topic, e.g., 'describe python'"
    )
    response: str = Field(description="The generated description or answer.")


class WeatherData(BaseModel):
    apparent_temperature: float
    is_day: bool
    wind_speed: float
    precipitation: float


class WeatherResponse(BaseModel):
    prompt: str
    response: WeatherData


class WeatherResponseModel(BaseModel):
    data: WeatherResponse
