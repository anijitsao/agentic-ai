from pydantic import BaseModel, Field


class ChatRequestModel(BaseModel):
    prompt: str = "describe python"


class ChatResponse(BaseModel):
    prompt: str
    response: str


class ChatResponseModel(BaseModel):
    data: ChatResponse


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
