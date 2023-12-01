import requests

url_todos = 'https://dummyjson.com/todos/'

response = requests.get(url=url_todos)
# print(response)
# print(response.content)
# print(response.text)
data_from_net = response.json()

print(data_from_net)
