from agents import Agent
from src.models import ChatResponseModel
from src.tools import fetch_activities, fetch_weather

from .format_response_agent import get_format_response_agent

format_agent = get_format_response_agent(ChatResponseModel)
get_suggest_activity_agent = Agent(
    name="SuggestActivityAgent",
    instructions="""You are an agent who can
    - Answers indoor and outdoor activity for a city
    - First extract the city from the prompt
    - Fetch weather of the city using the fetch_weather tool passing the city name.

    - Now use the search_activity tool and use temperature, wind_speed, humidity, is_day, rain, snowfall, precipitation.
    - Perform RAG
    - To format the response please hanoff to format_agent
    """,
    tools=[fetch_weather, fetch_activities],
    # As Groq does not support both Tool Calling and Structured Response
    # in one Agent we have created another smaller agent which can perform
    # the same.
    # output_type=WeatherResponseModel,
    handoffs=[format_agent],
)
