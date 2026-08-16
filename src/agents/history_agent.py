from agent_framework import Agent
from src.tools.fetch_weather_tool import fetch_weather

# from src.models.weather_model import ChatResponse


async def create_history_agent(client):
    try:
        history_agent = Agent(
            name="HistoryAgent",
            client=client,
            instructions="""You are an agent who can " 
           explain things briefly within 2-3 sentences.

           Whenever you are asked to fetch weather of a city you just 
           extract the city name and use the fetch_weather tool using the city name.

           """,
            tools=[fetch_weather],
        )
        return history_agent
    except Exception as e:
        print("error occcurred", e)
        return e
