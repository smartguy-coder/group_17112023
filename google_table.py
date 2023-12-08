import requests
# url = 'https://script.google.com/macros/s/AKfycbzQl4kN94Ae9dNvXPy7QS9nmvBMuYi5eJK9bh2XJmJzrNrKmpDl9KoBlWUGTt-QeT-R/exec'
#
# response = requests.get(url=url)
# data_from_net = response.json()
# print(data_from_net)

url = 'https://script.google.com/macros/s/AKfycbwvUKAQc8b3-AxE2TCm16JPSX9hLeUJCc_g-zcngDCu0K7LfHFQ-2xV3u50gfnhWvgs/exec'
response = requests.get(url=url)
data_from_net = response.json()
print(data_from_net)
