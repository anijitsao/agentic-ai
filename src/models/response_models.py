from pydantic import BaseModel


class ChatRequestModel(BaseModel):
    prompt: str = "describe python"


class ChatResponse(BaseModel):
    prompt: str
    response: str


class ChatResponseModel(BaseModel):
    data: ChatResponse

class WeatherData(BaseModel):
    temperature: float
    is_day: bool
    wind_speed: float
    relative_humidity: float
    precipitation: float
    rain: float
    snowfall: float

class WeatherResponse(BaseModel):
    prompt: str
    response: WeatherData

class WeatherResponseModel(BaseModel):
    data: WeatherResponse
