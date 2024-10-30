import requests

API_KEY = 'b46a25a3682bb69e375013652fcb6be8'
URL = 'http://api.weatherstack.com/current'


def get_weather(city):
    search_param = {
        'access_key': API_KEY,
        'query': city
    }
    response = requests.get(URL, params=search_param)
    return f'На данный момент температура в г.{city}: {response.json()['current']['temperature']}'
