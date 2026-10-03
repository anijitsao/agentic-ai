import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from agents import set_default_openai_client

# loads all the environment variables
load_dotenv()

ollama_client = AsyncOpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

set_default_openai_client(ollama_client)
