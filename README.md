# python-app-simple-weather-n-play-ai
This example illustrates various concepts of Agentic AI System using [Python](https://www.python.org/) and [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/). This is multiple agents system where agents can have tools, can communicate using handoffs, filter user input prompts using guardrails. User can asks for current weather about their current city (worldwide) and the system will give them suggestion about games and activities based on the weather conditions. Agents can search their Knowledge Base and predict using Retrival Augmented Generation (RAG).

## Features 
- Multiple Agents are supported
  - `TriageAgent` redirects the user prompt to corresponding agent based on handoff direction.
  - `WeatherAgent` uses function tools to find the weather of the current city.
  - `GKAgent` gives answers to General Knowledge questions.
  - `SuggestActivityAgent` suggests activities and games based on the current weather conditions.
  - `FormatResponseAgent` format the responses to JSON.

- **Tool calling** is supported through python functions.
- User prompts are filtered through guardails to remove *profanity*.
- Redirection to various agents is supported through **Handoffs**.  
- Response formats are supported using [Pydantic](https://pydantic.dev/docs/validation/latest/get-started/).
- [Sqlite](https://www.sqlite.org/) based sessions are used for Agent Memory.
 

- For agents orchestration, [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) is used. 
  - to see [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?pivots=programming-language-python) based orchestration please check [here](https://github.com/anijitsao/python-app-simple-weather-n-play-ai/tree/MAF).

- [Groq](https://console.groq.com/docs/quickstart) cloud APIs are used for foundation model purpose. Please make sure you have the API Key to access Groq [Groq](https://console.groq.com/docs/quickstart).
  - Local LLM based foundation models are also supported using [Ollama](https://docs.ollama.com/). Please check [here](https://github.com/anijitsao/python-app-simple-weather-n-play-ai/tree/ollama).
- REST APIs are served using [FastAPI](https://fastapi.tiangolo.com/).

- For vector store [ChromaDB](https://www.trychroma.com/) is used.

### Install
To install all the dependencies please use the following commands from a shell/ Terminal. For package management purpose [uv](https://docs.astral.sh/uv/) is used. However some of `pip` commands are also listed.

##### uv based shell commands
Please use the following commands from a shell / Terminal.

```shell
git clone https://github.com/anijitsao/python-app-simple-weather-n-play-ai.git

# Navigate into the directory
cd python-app-simple-weather-n-play-ai

# Activate the virtual environment
source .venv/bin/activate  # Linux
.venv\Scripts\activate # Windows

# Install all those dependencies
uv sync
```

> :exclamation: Please make sure you have run the `ingestion.py` before running the FastAPI application. This will create the vector store for **Retrival Augmented Generation**.

```shell
python ingestion.py
```

Now to run the application please use the following commands

```shell
# Navigate to the directory
cd python-app-simple-weather-n-play-ai

# Run the FastAPI server
uv run fastapi dev app.py # development
uv run fastapi run app.py # production
```

Please visit [http://localhost:8000/docs](http://localhost:8000/docs) and play with the agents!

#### pip based useful commands
```shell
# creates a Virtual environment
python -m venv .venv  

# It will install all the dependencies listed in requirements.txt file
pip install -r requirements.txt 

# Run the code
python main.py
```
