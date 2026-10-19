from agents import Agent
from src.models import WeatherResponseModel
from src.tools import fetch_weather

from .format_response_agent import get_format_response_agent

format_agent = get_format_response_agent(WeatherResponseModel)
get_weather_agent = Agent(
    name="WeatherAgent",
    instructions="""You are an agent who can
    - fetch weather and predict it.

    - Whenever you are asked to fetch weather of a city you just
    extract the city name and use the fetch_weather tool using the city name.
    - To format the response please hanoff to format_agent
    """,
    tools=[fetch_weather],

    # As Groq does not support both Tool Calling and Structured Response
    # in one Agent we have created another smaller agent which can perform
    # the same.
    # output_type=WeatherResponseModel,
    handoffs=[format_agent]
)
