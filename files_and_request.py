from pprint import pprint
import time
import datetime as dt

import requests

# url_products = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
url_weather = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Odesa',
    'appid': '47503e85fabbabc93cff28c52398ae97',
    'units': 'metric',
}
# temp = 0
# for _ in range(10000):
# while temp < 10:
#     response = requests.get(url=url_weather, params=params)
#     data_from_net = response.json()
#     # pprint(data_from_net)
#     temp = data_from_net["main"]["temp"]
#     print(f'Зараз в Одесі {temp} градусів')
#     time.sleep(5)
#     # break
#
# while True:
#     response = requests.get(url=url_weather, params=params)
#     data_from_net = response.json()
#     # pprint(data_from_net)
#     temp = data_from_net["main"]["temp"]
#     city = params['q']
#     current_time = dt.datetime.now()
#
#     with open('weather_data.csv', mode='a', encoding='utf-8') as file:
#         file.write(f'{current_time};{city};{temp}\n')
#
#     time.sleep(5)
#     if temp >= 10:
#         break

with open('weather_data.csv', mode='r', encoding='utf-8') as file:
    # file_content = file.read().strip()
    # file_splited = file_content.split('\n')
    # # print(file_splited)
    # for line in file_splited:
    #     print(line.split(';'))

    # for line in file.readlines():
    #     temp = float(line.split(';')[-1])
    #     if temp > 10:
    #         print(temp)
    #
    #     if line.split(';')[1] == 'Dnipro':
    #         print(line)

    print(file.readline())
    print(file.readline())
    print(file.readline())


with open('weather_data1', mode='w', encoding='utf-8') as file:
    file.write('1111111111\n')
    file.write('2222222222223\n')

with open('weather_data1', mode='w', encoding='utf-8') as file:
    file.write('33333\n')
    file.write('4444444444\n')
#
# flag = True
#
# while flag:
#     response = requests.get(url=url_weather, params=params)
#     data_from_net = response.json()
#     # pprint(data_from_net)
#     temp = data_from_net["main"]["temp"]
#     print(f'Зараз в Одесі {temp} градусів')
#     time.sleep(5)
#     if temp >= 10:
#         flag = False

# while True:
#     user_age = input('Enter yor age, and get twice candies (integer number) >> ')
#     if user_age.isdigit():
#         print('Thank you')
#         break
#     print('You have entered not an integer')
#     print('Integers are like 5, 25, 60')
#
# user_age = int(user_age)
# candies = user_age * 2
# print(f'{candies=}')
# print('finish')











