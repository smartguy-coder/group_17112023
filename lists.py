# cities = 'Odesa, Vinnytsa, Dnipro'.split()
# result = ['Odesa,', 'Vinnytsa,', 'Dnipro']

# cities = 'Odesa,  Vinnytsa,  Dnipro'.split(',  ')
# result = ['Odesa', 'Vinnytsa', 'Dnipro']
# print(cities)

new_list1 = []
new_list2 = list()
new_list3 = [3806765646546, "+38135743435465", 55.66, [6, 5]]

list_of_products = [
    "cheese",
    "broccoli",
    "bread",
    "ice-cream",
]

sister_list_of_product = [
    "candies",
    "lipstick",
]

first_product = list_of_products[0]
# second_product = list_of_products[1]
# # ice_cream = list_of_products[50]
#
# # print(f'{first_product=}')
# # print(f'{second_product=}')
#
# for product in list_of_products:
#     print(product)
#     print(222222222)
#     print('***********')
#
# print('finish')


#                             delete element
list_of_products.remove("ice-cream")  # no elem - error
# deleted = list_of_products.pop()
deleted = list_of_products.pop(0)
# print(deleted)
# print(list_of_products)

#                             add element
list_of_products.append("milk")
list_of_products.insert(0, "beer")
# print(list_of_products)

# dealing with 2 lists
# 2 in 1
# list_of_products.extend(sister_list_of_product)
# list_of_products = list_of_products + sister_list_of_product
# list_of_products += sister_list_of_product
# print(list_of_products)
# new 1 + 1
new_products_list = list_of_products + sister_list_of_product
# print(new_products_list)
# print(list_of_products)


length = len(new_products_list)
# print(length)

# slices
print(new_products_list)
# first_three_products = new_products_list[:] - total copy
first_three_products = new_products_list[:3]
print(first_three_products)

forth_and_fifth = new_products_list[3:5]
print(forth_and_fifth)

last_product = new_products_list[-1]
print(last_product)

last_3_product = new_products_list[-3:]
print(last_3_product)

# get index of the element
brother_wish = "beer"
position = new_products_list.index(brother_wish)
print(position)


# string_into_list = list('qwerty')
# print(string_into_list)

sentence = "I love python"

for letter in sentence:
    upper_letter = letter.upper()
    print(upper_letter)

numbers = "22226565222223"

for number in numbers:
    int_mult_by_2 = int(number) * 2
    print(int_mult_by_2)
