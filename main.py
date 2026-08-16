# import asyncio
import os
from fastapi import FastAPI
# from dotenv import load_dotenv


from contextlib import asynccontextmanager
from src.utils.ollama_client_util import ollama_client

from src.routes import ai_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ollama_client = ollama_client
    print("Ollama client initialized")
    yield


# initialize the FastAPI app
app = FastAPI(
    description=os.getenv("APP_DESCRIPTION"),
    title=os.getenv("APP_NAME"),
    lifespan=lifespan,
)

print(f"app name: {os.getenv('APP_NAME')}")


# asyncio.run(main("What is India?"))


@app.get("/")
async def index_route():
    return {"message": "API reached"}


@app.get("/about")
async def about_page():
    return {"message": "About page"}


app.include_router(ai_router)
