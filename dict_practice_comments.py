import requests

url_comments = 'https://dummyjson.com/comments?limit=340'

response = requests.get(url=url_comments)
data_from_net = response.json()  # dict
comments = data_from_net['comments']  # list of dicts

for comment in comments:
    if comment['user']['id'] == 31:
        print(comment['body'])
