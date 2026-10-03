from fastapi import APIRouter, HTTPException, status

from agents import Agent, ModelSettings, Runner

# from src.agents.history_agent import create_history_agent
from src.models import ChatRequestModel, ChatResponseModel

router = APIRouter(tags=["agentic-ai"])


@router.post("/question/", response_model=ChatResponseModel)
async def generate_response_from_prompt(req: ChatRequestModel):
    try:
        history_agent = Agent(
            name="HistoryAgent",
            instructions="""You are a  history agent who can explain things shortly.
                - Keep response to 10 words or fewer
                """,
        )
        response = await Runner.run(starting_agent=history_agent, input=req.prompt)
        print("Hello from openai-agents!", response)

        return {"data": {"prompt": req.prompt, "response": response.final_output}}
    except Exception as e:
        print("error occcurred", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent execution failed: {str(e)}",
        )
