from pprint import pprint

import requests

# url_products = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
url_weather = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Одеса',
    'appid': '47503e85fabbabc93cff28c52398ae97',
    'units': 'metric',
}

response = requests.get(url=url_weather, params=params)
data_from_net = response.json()
pprint(data_from_net)
print(f'Зараз в Одесі {data_from_net["main"]["temp"]} градусів')