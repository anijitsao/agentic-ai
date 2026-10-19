from fastapi import APIRouter

from src.models import (
    ChatRequestModel,
    ChatResponseModel,
    ErrorModel,
)
from src.services import get_question_answer_service, get_weather_service

router = APIRouter(tags=["agentic-ai"])


@router.post(
    "/question/",
    responses={
        200: {"model": ChatResponseModel, "description": "Successful Response"},
        400: {"model": ErrorModel, "description": "Invalid Input Data"},
        500: {"model": ErrorModel, "description": "Internal Server Error"},
    },
)
async def generate_response_from_prompt(req: ChatRequestModel):
    await get_question_answer_service(req)


@router.get(
    "/get-weather/{city}",
    responses={
        200: {"model": ChatResponseModel, "description": "Successful Response"},
        400: {"model": ErrorModel, "description": "Invalid Input Data"},
        500: {"model": ErrorModel, "description": "Internal Server Error"},
    },
)
async def predict_weather(city: str = "Kolkata"):
    await get_weather_service(city)
