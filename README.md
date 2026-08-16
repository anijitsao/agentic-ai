# Agentic AI using python
This example illustrates various concepts of AI agents using python and Microsoft Agents Framework. To run and test all those AI Agents locally we are using Ollama models. 

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
