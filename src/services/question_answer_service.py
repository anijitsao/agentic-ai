from fastapi import HTTPException, status

from agents import Runner
from src.agents import get_triage_agent

# classifier_agent = get_classifier_agent("""You are an agent who can
#     - Determine the user input has any vulgar words, asking for making lethal weapons
#     - asking to kill human beings, animals
#
#     - If you found anything like that set is_information_related to False
#     """)


async def get_question_answer_service(req):
    try:
        response = await Runner.run(
            get_triage_agent,
            input=req.prompt,
            # context={"classifier_agent": classifier_agent},  # Groq doesn't support Guardrails
        )
        print("Hello from openai-agents!", response)
        return response.final_output
    except Exception as e:
        print("error occcurred", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent execution failed: {e!s}",  # same as str(e)
        )
