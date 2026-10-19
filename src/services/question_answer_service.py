from fastapi import HTTPException, status

from agents import Runner
from src.agents import get_triage_agent


async def get_question_answer_service(req):
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
