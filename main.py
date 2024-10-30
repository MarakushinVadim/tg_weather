import requests

BOT_TOKEN = '6645562060:AAEr_Lr-Eb0_SQG4KlG6c-GYups4wJiOns8'
TG_URL = 'https://api.telegram.org/bot'

API_KEY = 'b46a25a3682bb69e375013652fcb6be8'
URL = 'http://api.weatherstack.com/current'

search_param = {
    'access_key': API_KEY,
    'query': 'оймякон'
}

response = requests.get(URL, params=search_param)

print(response.json()['current']['temperature'])
