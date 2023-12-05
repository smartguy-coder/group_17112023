import requests

url_products = 'https://dummyjson.com/users'
params = {'limit': 100, 'skip': 0}

response = requests.get(url=url_products, params=params)
data_from_net = response.json()
users = data_from_net['users']

names = []
for user in users:
    # None == 'Washington'
    if user['address'].get('city') == 'Washington':
        names.append(f'{user["firstName"]} {user["lastName"]}')
print(names)
