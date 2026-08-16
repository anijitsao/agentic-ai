import os
from agent_framework.ollama import OllamaChatClient
from dotenv import load_dotenv

# loads all the environment variables
load_dotenv()

print("model name", os.getenv("OLLAMA_MODEL"))
ollama_client = OllamaChatClient(model=os.getenv("OLLAMA_MODEL"))
