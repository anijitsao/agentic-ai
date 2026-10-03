# import asyncio
import os

# from dotenv import load_dotenv
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.routes import ai_router, default_router
from src.utils import ollama_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ollama_client = ollama_client
    print("Ollama client initialized")
    yield


# initialize the FastAPI app
app = FastAPI(
    description=os.getenv("APP_DESCRIPTION", "Agentic AI app"),
    title=os.getenv("APP_NAME", "Agentic AI"),
    lifespan=lifespan,
)

print(f"app name: {os.getenv('APP_NAME')}")


app.include_router(default_router)
app.include_router(ai_router)
