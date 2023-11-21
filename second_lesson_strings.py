# name = 'Alex'
# surname = 'Clinton ✄'
#
# reaction = '\U00002601'
#
# # full_name = name + ' ' + surname + ' ' + reaction
# # another approach
# full_name = f'{name} {surname} - {reaction}  another text'
#
# print(full_name)
# print(reaction)
#
# print('-*- ' * 10)
#
# another_string = '   \n    \t     555djkbdfkjbhjkdfb dfhbj4565649956'
# no_whitespaces = another_string.strip()
# another_string = '5+++++++++++++++++++++++++'
#
# print(no_whitespaces)
# print(another_string)
#
# print('-*- ' * 10)
#
# poem = """
# \tЯк умру то поховайте
# Мене на Вкраїні
# """
#
# poem = '\tЯк умру то поховайте\nМене на Вкраїні'
#
# print(poem, another_string, sep='_______', end='***')
# print('pppppp')

city_slogan = "         i ❤ odesa"
# city_slogan = city_slogan.strip().title().capitalize()
city_slogan = city_slogan.strip().title()

print(city_slogan)

some_string = "56HHHHJKkkkkkk5656'         ß"
print(some_string)

print(some_string.isdigit())
False
processed_string = some_string.strip("'")
print(processed_string.isdigit())
True
print(processed_string.casefold())
print(processed_string.lower())
print(processed_string.upper())

print(len(some_string))
print(some_string.count("k"))
print(ord("\U00002601"))
print(ord("+"))
print(chr(43))

print("aa" == "A")
# print('555' > '1000')
# print('aa' < 'A')

print(some_string.startswith("56H"))
print(some_string.endswith(" ß"))

print("odesa" in city_slogan.lower())
