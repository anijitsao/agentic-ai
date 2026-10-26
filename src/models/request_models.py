from pydantic import BaseModel, Field


class ChatRequestModel(BaseModel):
    prompt: str = Field(
        default="Please describe python",
        description="The prompt you want to send to the agent",
        examples=["Please describe Python", "What is India?"],
    )


class WeatherRequestModel(BaseModel):
    city: str = "Kolkata"
