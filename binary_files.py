import requests

url_image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/XN_Fruehjahrswiese_00.jpg/250px-XN_Fruehjahrswiese_00.jpg'

response = requests.get(url=url_image)

content = response.content

with open('spring.jpg', mode='wb') as file:
    file.write(content)


with open('spring.jpg', mode='ab') as file:
    file.write(b'hello from python')


with open('spring.jpg', mode='rb') as file:
    data = file.read()
    print(data)