from agents import Agent
from src.guardrails import classify_input_guardrails

# from src.guardrails import classify_input_guardrails
from .gk_agent import get_gk_agent
from .suggest_activity_agent import get_suggest_activity_agent
from .weather_agent import get_weather_agent

get_triage_agent = Agent(
    name="TriageAgent",
    instructions="""You are an agent who can
    - Triage questions to multiple agents
    - be polite and positive
    - Whenever you are asked general knowledge questions redirect it to GKAgent.
    - When you are asked weather related questions redirect it to WeatherAgent.
    - When you are asked to suggest activities at a city redirect it to SuggestActivityAgent.
    """,
    handoffs=[get_gk_agent, get_weather_agent, get_suggest_activity_agent],
    # Groq doesn't support Guardrails
    input_guardrails=[classify_input_guardrails],
    # output_type=ChatResponseModel
    # As Groq does not support both Tool Calling and Structured Response
    # in one Agent we have created another smaller agent which can perform
    # the same.
    # output_type=WeatherResponseModel,
)
