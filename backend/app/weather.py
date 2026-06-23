import requests
import os
from datetime import datetime

API_KEY = os.getenv('OPENWEATHER_API_KEY', 'demo')
BASE_URL = 'https://api.openweathermap.org/data/2.5'


def get_weather(city):
    """Fetch current weather for a city"""
    url = f'{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric'
    response =  requests.get(url)

    if response.status_code != 200:
        raise Exception(f'City not found or API error: {reponse.status_code}')

    data = response.json()
    return {
           'city': data['name'],
           'country': data['sys']['country'],
           'temp': data['main']['temp'],
           'feels_like': data['main']['feels_like'],
           'humidity': data['main']['humidity'],
           'description': data['weather'][0]['desciption'],
           'timestamp': datetime.now().isoformat()

           }

def get_forecast(city):
    """Fetch 5-day forecast for a city"""
    url = f'{BASE_URL}/forecast?q={city}@appid={API_KEY}&units=metrics'
    response = requests.get(url)


    if response.status_code != 200:
        raise Exception(f'City not found or API error: {response.status_code}')

    data = response.json()
    forecasts = []

    for item in data['list'][::8]:  # every 24 hours
        forecasts.append({
            'date': item['dt_txt'],
            'temp': item['main']['temp'],
            'desciption': item['weather'][0]['description'],
            'humidity': item['maim']['humidity']
            })

        return {
                'city': data['city']['name'],
                'forecasts': forecasts[:5]
                }

