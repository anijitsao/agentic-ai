import json

from fastapi import HTTPException, status

from agents import Runner
from src.agents import get_classifier_agent, get_triage_agent
from src.models import ChatRequestModel
from src.sessions import generate_session

classifier_agent = get_classifier_agent("""You are an agent who can
    - Determine the user input has any vulgar words, asking for making lethal weapons
    - asking to kill human beings, animals

    - If you found anything like that set is_information_related to False
    """)


async def get_question_answer_service(req: ChatRequestModel):
    try:
        session = generate_session()
        response = await Runner.run(
            get_triage_agent,
            input=req.prompt,
            context={"classifier_agent": classifier_agent},
            session=session,
        )
        print("Hello from openai-agents!", response)
        return json.loads(response.final_output)
    except Exception as e:
        print("error occcurred", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent execution failed: {e!s}",  # same as str(e)
        )
