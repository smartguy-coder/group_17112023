def get_unique_names(names: list[str]) -> list[str]:

    processed_names = []
    for name in names:
        processed_name = name.strip().title()
        if processed_name not in processed_names:
            processed_names.append(processed_name)

    return processed_names


operations = {
    'mult2': lambda n: n * 2,
    'mult3': lambda n: n * 3,
    'mult4': lambda n: [555, 66, 89898],
    'print': print,
}

# user_command = input('--->>> ')
# user_number = int(input('number --->>> '))
#
#
# result = operations.get(user_command, lambda n: 6666)(user_number)
# print(result)



# map filter

my_list = ['alex', '          Alex', 'julia', 'john', '555']


def process_string(value: str) -> str:
    processed_value = value.strip().title()
    return processed_value


processed_strings = map(process_string, my_list)
# processed_strings = map(lambda s: s.strip().title(), my_list)
# print(list(processed_strings))

# l = []
#
# for i in range(1_000_000_000):
#     l.append(i)
#     print(i)

# nl = map(lambda n: n, range(1_000_000_000))
# print(3333333)
# print(nl)


# filtered_data = filter(lambda s: 'a' in s.lower(), processed_strings)
filtered_data = filter(lambda s: 'a', processed_strings)

print(list(filtered_data))
print(list(filtered_data))


