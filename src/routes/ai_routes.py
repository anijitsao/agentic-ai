import os

from fastapi import APIRouter, Request

from agents import Agent, Runner

# from src.agents.history_agent import create_history_agent
from src.models import ChatResponseModel

router = APIRouter(tags=["egentic-ai"])


@router.get("/question/", response_model=ChatResponseModel)
async def generate_response_from_prompt(req: Request, query: str = "what is python?"):
    try:
        history_agent = Agent(
            name="HistoryAgent",
            instructions="""You are a  history agent who can explain things shortly.
                Please describe the things very shortly within 20 words.
                """,
            model=os.getenv("MODEL_NAME"),
        )
        response = await Runner.run(starting_agent=history_agent, input=query)
        print("Hello from openai-agents!")

        return {"data": {"prompt": query, "response": response.final_output}}
    except Exception as e:
        print("error occcurred", e)
