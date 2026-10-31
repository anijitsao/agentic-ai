# python-app-simple-weather-n-play-ai.git
This example illustrates various concepts of Agentic AI System using python and OpenAI Agents SDK. This is multiple agents system where agents can have tools, can communicate using handoffs, filter user input prompts using guardrails. User can asks for current weather about their current city (worldwide) and the system will give them suggestion about games and activities based on the weather conditions. Agents can search their Knowledge Base and predict using Retrival Augmented Generation (RAG).

## Todo 
We will serve several endpoint using `FastAPI` through which our agents will work

### Ollama service
To make sure that Ollama is running please navigate your browser to [http://localhost:11434/](http://localhost:11434/). If nothing is shown there please use the following command to run the Ollama Service.

```shell
# List all the installed models in Ollama
ollama list

# To run a model e.g. smollm2:135m in interactive mode
ollama run smollm:135m

# To run the ollama service
ollama serve
```


### Install
To install all the dependencies please use the following commands from a shell/ Terminal

```shell
# creates a Virtual environment
python -m venv .venv  

# It will install all the dependencies listed in requirements.txt file
pip install -r requirements.txt 

# Run the code
python main.py
```
