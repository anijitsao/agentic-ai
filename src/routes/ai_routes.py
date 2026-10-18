from fastapi import APIRouter, HTTPException, status

from agents import Runner
from src.agents import get_gk_agent, get_triage_agent, get_weather_agent

# from src.agents.history_agent import create_history_agent
from src.models import (
    ChatRequestModel,
    ChatResponseModel,
    ErrorModel,
)

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
    try:
        response = await Runner.run(get_triage_agent, input=req.prompt)
        print("Hello from openai-agents!", response)
        print("Final Output", response.final_output)
        return response.final_output
    except Exception as e:
        print("error occcurred", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent execution failed: {str(e)}",
        )


@router.get(
    "/get-weather/{city}",
    responses={
        200: {"model": ChatResponseModel, "description": "Successful Response"},
        400: {"model": ErrorModel, "description": "Invalid Input Data"},
        500: {"model": ErrorModel, "description": "Internal Server Error"},
    },
)
async def predict_weather(city: str = "Kolkata"):
    try:
        response = await Runner.run(
            get_weather_agent, input=f"what is the weather of {city}"
        )
        # print("weather is: ", response.final_output)
        return {
            "data": {"prompt": f"weather of {city}", "response": response.final_output}
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent execution failed: {str(e)}",
        )
