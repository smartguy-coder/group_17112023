person = {
    'name': 'Igor',
    'age': 45,
    'hobbies': [
        'reading',
        'swimming',
    ],
    'salary': None,
    'surname': 'Clinton',
    (5, ): 55,
    'action': print,
    'dict_func': dict,
}

# person['action'](666666666)

# person2 = dict()
person3 = dict(name='Andrew', surname='Bush')


# retrieve data
person_one_name = person['name']
person_one_hobby_one = person['hobbies'][0]
# person_one_surname = person['surname']
# person_one_surname = person.get('surname')
person_one_surname = person.get('surname', '')
full_data = person_one_surname + person_one_name

salary_person_one = person.get('salary') or 0
ndfl = salary_person_one * 0.18

# false data: 0, 0.0, '', None, {}, False

# add data
car = {'brand': 'audi', 'power': 356, 'engine_volume': 6.4}

person['car'] = car
person['age'] = 35

person_car_engine_volume = person['car']['engine_volume']

# delete data
# del person['car']
# del person
# person3['car'] = person.pop('car')

# for attribute in person:
#     print(attribute)
#     print(f'{attribute} = {person[attribute]}')
#     print('*' * 50)

# print(person.keys())
# print(person.values())
print(person.items())
print(print())

# for attribute in person.keys():
# for attribute in person.values():
# for item in person.items():
#     print(item)
#     print(type(item))
#     key = item[0]
#     value = item[1]
#     print('*' * 50)

something = ('name', 'Igor')
something2 = 'name', 'Igor', 'third_value', 'forth_value'
key, value, *args = something

data = 5,

for key, value in person.items():
    print(value)
    print('*' * 50)
    print()


print(key)

# some_list = ['name', 'Igor']
# some_tuple = ('name', 'Igor')
# n = some_tuple[0]
# some_list.pop()
# print(some_list)
