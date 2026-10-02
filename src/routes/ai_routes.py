import os

from dotenv import load_dotenv
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent

from agents import Agent, Runner, set_default_openai_client, set_tracing_disabled

# from src.agents.history_agent import create_history_agent

# from src.utils.ollama_client_util import ollama_client

load_dotenv()
ollama_client = AsyncOpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

set_default_openai_client(ollama_client)


router = APIRouter(tags=["egentic-ai"])


@router.get("/question/")
async def main(req: Request, query: str = "what is python?"):
    try:
        # print("result: ", result.text)

        history_agent = Agent(
            name="HistoryAgent",
            instructions="""You are a  history agent who can explain things shortly.
                Please describe the things very shortly within 20 words.
                """,
            model=os.getenv("MODEL_NAME"),
        )
        response = await Runner.run(starting_agent=history_agent, input=query)
        print("Hello from openai-agents!")

        #         async for event in response.stream_events():
        #             if event.type == "raw_response_event" and isinstance(
        #                 event.data, ResponseTextDeltaEvent
        #             ):
        #                 content = event.data.delta
        #                 print(content, end="", flush=True)
        #
        #             print("\n")
        #
        return {"data": {"prompt": query, "response": response.final_output}}
    except Exception as e:
        print("error occcurred", e)
