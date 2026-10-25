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

    - Now use the search_activity tool and use apparent_temperature, wind_speed, is_day, and precipitation.
    - And use the tool fetch_activities to find the activities and games
    - Please suggest the activities and games based on the documents supplied to you.
    - To format the response please handoff to format_agent
    """,
    tools=[fetch_weather, fetch_activities],
    # As Groq does not support both Tool Calling and Structured Response
    # in one Agent we have created another smaller agent which can perform
    # the same.
    # output_type=WeatherResponseModel,
    handoffs=[format_agent],
)
