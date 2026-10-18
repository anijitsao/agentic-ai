from agents import Agent
from src.models import ChatResponseModel

from .gk_agent import get_gk_agent
from .weather_agent import get_weather_agent

get_triage_agent = Agent(
    name="TriageAgent",
    instructions="""You are an agent who can
    - Triage questions to multiple agents
    - be polite and positive
    - Whenever you are asked general knowledge questions redirect it to GKAgent.
    - When you are asked weather related questions redirect it to WeatherAgent.

    """,
    handoffs=[get_gk_agent, get_weather_agent],
    output_type=ChatResponseModel
)
