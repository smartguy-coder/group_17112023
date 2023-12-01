from pprint import pprint

import requests

url_todos = 'https://dummyjson.com/todos/'

response = requests.get(url=url_todos)
# print(response)
# print(response.content)
# print(response.text)
data_from_net = response.json()

todos = data_from_net['todos']

for todo in todos:
    print(todo)


