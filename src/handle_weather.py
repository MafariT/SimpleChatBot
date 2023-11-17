import geocoder
import requests
import datetime
from src.logger import logger
from src.config import WEATHER_API_KEY


def get_location() -> tuple:
    g = geocoder.ip('me')
    return g.city, g.latlng

def get_forecast(lat: float, lon: float) -> dict:
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric'
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def format_temperature_data(data: dict) -> tuple:
    temperature_data = []
    time_data = []
    for forecast_entry in data['list'][:8]:
        temperature = forecast_entry['main']['temp']
        timestamp = forecast_entry['dt']
        temperature_data.append(temperature)
        time_data.append(datetime.datetime.fromtimestamp(timestamp))

    return time_data, temperature_data

def format_weather_data(data: dict) -> list:
    weather_data = []
    for forecast_entry in data['list']:
        timestamp = forecast_entry['dt']
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        temperature = forecast_entry['main']['temp']
        humidity = forecast_entry['main']['humidity']
        description = forecast_entry['weather'][0]['description']
        weather_data.append((date, temperature, humidity, description))

    return weather_data

def group_weather_data(weather_data: list) -> dict:
    grouped_weather_data = {}
    for date, temperature, humidity, description in weather_data:
        grouped_weather_data.setdefault(date, []).append((temperature, humidity, description))

    return grouped_weather_data

def get_weather_info() -> str:
    try:
        city, (lat, lon) = get_location()

        data = get_forecast(lat, lon)

        if data:
            time_data, temperature_data = format_temperature_data(data)
            weather_data = format_weather_data(data)
            grouped_weather_data = group_weather_data(weather_data)

            # Format the weather information into a response
            response = f"\nThe current temperature is {temperature_data[0]} degrees Celsius. The weather is {weather_data[0][3]} in {city}\n\n"
            response += f"Here's the temperature forecast for the next 24 hours in {city}:\n\n"
            response += "- " + "\n- ".join([f"{time_data[i].strftime('%Y-%m-%d %H:%M:%S')}: {weather_data[i][3]}, {temperature_data[i]} degrees Celsius, " for i in range(len(time_data))])
            response += f"\n\nHere's the weather forecast for the next 5 days in {city}:\n"
            for date, weather_list in grouped_weather_data.items():
                average_temperature = sum([t for t, h, _ in weather_list]) / len(weather_list)
                average_humidity = sum([h for _, h, _ in weather_list]) / len(weather_list)
                description = weather_list[0][2]
                response += f"\n{date}: {description}, {average_temperature:.1f} degrees Celsius, {average_humidity:.0f}% humidity"
        else:
            response = "Sorry, I couldn't retrieve the weather information at this time."
    except Exception as e:
        logger.error(f"An error occurred while retrieving the weather information. Exception: {e}", exc_info=True)
        response = "An error occurred while retrieving the weather information. Please check the log file for more information on the error"

    return response



