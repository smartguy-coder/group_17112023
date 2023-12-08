import requests

url_currency = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

response = requests.get(url=url_currency)
data_from_net = response.json()  # list

for currency in data_from_net:
    result = f'{currency["txt"]} зараз коштує {currency["rate"]}'
    print(result)
