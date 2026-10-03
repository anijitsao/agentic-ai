import requests
from agents.decorators import tool


# @tool
def fetch_weather(city: str):
    try:
        # Step 1: Fetch Lat, Long of the city provided
        geo_res = requests.get(
            url= "https://geocoding-api.open-meteo.com/v1/search",
            params= {
                "name": city,
                "count": 1
            },
            timeout=5
        ).json()
        latitude = geo_res["results"][0]["latitude"]
        longitude = geo_res["results"][0]["longitude"]

        # Step 2: Fetch current temperature
        weather_data = requests.get(
            url="https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": [
                    "temperature_2m",
                    "is_day",
                    "wind_speed_10m",
                    "relative_humidity_2m",
                    "precipitation",
                    "rain",
                    "snowfall",
                ],
            },
            timeout=5
        ).json()

        current_weather_data = weather_data["current"]

        # print("response received", current_weather_data)
        return current_weather_data
    except Exception as e:
        print("unable to fetch weather", e)
        raise e


print(fetch_weather(city="Kolkata"))
