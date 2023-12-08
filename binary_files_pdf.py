import requests

url_pdf = 'https://github.com/progit/progit2/releases/download/2.1.412/progit.pdf'

response = requests.get(url=url_pdf)

content = response.content

with open('file.pdf', mode='wb') as file:
    file.write(content)


with open('file.pdf', mode='ab') as file:
    file.write(b'hello from python')


with open('file.pdf', mode='rb') as file:
    data = file.read()
    print(data)
