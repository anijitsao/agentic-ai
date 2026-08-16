import requests
from agent_framework import tool


@tool
def fetch_weather(city: str):
    # response = requests.get(f"https://wttr.io/{city}?format=j1")
    # weather_data = response.json()
    # print("response received", weather_data)
    return "Weather of Kolkata is 15C"
