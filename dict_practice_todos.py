from pprint import pprint

import requests

url_todos = 'https://dummyjson.com/todos/'

response = requests.get(url=url_todos)
# print(response)
# print(response.content)
# print(response.text)
# print(response.json())
data_from_net = response.json()

todos = data_from_net['todos']  # list of dicts

for todo in todos:
    # print(todo)
    #      {'id': 12, 'todo': 'Organize pantry', 'completed': True, 'userId': 39}

    # get all completed todos
    # if todo['completed']:
    #     print(todo['todo'])

    # get all not completed todos
    # if not todo['completed']:
    #     print(todo['todo'])
    #     print(todo['completed'])

    # another approach
    # get all todos of the user #13
    # if todo['userId'] == 13:
    #     print(todo)

    # get all todos of the NOT user #13
    # if todo['userId'] != 13:
    #     print(todo)

    # get all todos of the user below #13
    # if todo['userId'] < 13:
    #     print(todo)

    # get all todos of the user above #13 include #13
    if todo['userId'] >= 13:
        print(todo)