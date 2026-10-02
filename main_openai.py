import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent

from agents import Agent, Runner, set_default_openai_client, set_tracing_disabled

load_dotenv()
ollama_client = AsyncOpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

set_default_openai_client(ollama_client)


async def main():
    history_agent = Agent(
        name="HistoryAgent",
        instructions="""You are a  history agent who can explain things shortly.
        Please describe the things very shortly within 250 words.
        """,
        model=os.getenv("MODEL_NAME"),
    )
    response = Runner.run_streamed(starting_agent=history_agent, input="What is India?")
    print("Hello from openai-agents!")

    async for event in response.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            content = event.data.delta
            print(content, end="", flush=True)

    print("\n")


if __name__ == "__main__":
    asyncio.run(main())
