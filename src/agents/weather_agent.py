from agents import Agent
from src.models import WeatherResponseModel
from src.tools import fetch_weather

get_weather_agent = Agent(
    name="WeatherAgent",
    instructions="""You are an agent who can
    - fetch weather and predict it.

    - Whenever you are asked to fetch weather of a city you just
    extract the city name and use the fetch_weather tool using the city name.

    """,
    tools=[fetch_weather],
    output_type=WeatherResponseModel,
)
