import requests

url_products = 'https://dummyjson.com/products'
params = {'limit': 100, 'skip': 0}

response = requests.get(url=url_products, params=params)
data_from_net = response.json()
products = data_from_net['products']

total_cost = 0
total_items = 0
for product in products:
    # if product['brand'] == 'Apple' and product['category'] == 'laptops':

    # if product['brand'] == 'Apple' or product['brand'] == 'Samsung':
    # if product['brand'] in ['Apple', 'Samsung']:
    brands = ['Apple', 'Samsung']
    # if product['brand'] in brands:
    if (product['brand'] in brands) and (product['category'] == 'laptops'):
        price = product['price']
        stock = product['stock']
        total_cost += price * stock
        total_items += stock

print(f'{total_cost=}')
print(f'{total_items=}')

if total_items:
    average_price = total_cost / total_items
    print(f'{average_price=}')
else:
    print('No data')


# url_products = 'https://dummyjson.com/products/{product_id}'
#
# pages = range(1, 100 + 1, 20)
# print(pages)
#
# for page in pages:
#     unique_product_url = url_products.format(product_id=page)
#     response = requests.get(url=unique_product_url)
#     data_from_net = response.json()
#     print(data_from_net)

# l = [3, 5, 6]
# s = sum(l)
