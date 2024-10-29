import requests

BOT_TOKEN = '?'
TG_URL = 'https://api.telegram.org/bot'

API_KEY = '?'
URL = 'http://api.weatherstack.com/current'

search_param = {
    'access_key': API_KEY,
    'query': 'оймякон'
}

response = requests.get(URL, params=search_param)

print(response.json()['current']['temperature'])
