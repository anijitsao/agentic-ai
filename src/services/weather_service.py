from fastapi import HTTPException, status

from agents import Runner
from src.agents import get_weather_agent


async def get_weather_service(city: str):
    try:
        response = await Runner.run(
            get_weather_agent, input=f"what is the weather of {city}"
        )
        return response.final_output
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent execution failed: {str(e)}",
        )
