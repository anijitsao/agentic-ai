from pydantic import BaseModel


class WeatherRequestModel(BaseModel):
    city: str = "Kolkata"
