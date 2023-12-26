# my_list = [5, 5, 88, 'jkhfgj']
#
# # create
# # 1
# set_var = set()
# print(set_var)
#
# # 2
# set_from_list = set(my_list)
# print(set_from_list)
#
# # 3
# set_with_data = {6, 6, 8989, 'hhh'}
# print(set_with_data)
#
#
# # practice
# cities = 'Lviv odesa Odesa Odesa Dnipro'
# cities_list = cities.title().split()
# cities_set = set(cities_list)
#
# print('Dnipro' in cities_list)
# print('Dnipro' in cities_set)
#
#
# def a_b_check(string: str) -> bool:
#     """
#     aaaaaaaaaabbbbbbbbb - True
#     aaaaaaaaaaaaa - True
#     bbbbbbbbbbbbbb - True
#     baaaaaaaaba  - False
#     """
#     print(set(string))
#     if len(set(string)) == 1:
#         return True
#
#     cleaned_string = string.rstrip('b')
#     if 'b' in set(cleaned_string):
#         return False
#     return True
#
#
# print(a_b_check('aaaabaaaaaaaaaaab'))
#
#
# for letter in set('ffff5656ffffjhfgjhgjhgjhgjg'):
#     print(letter)


new_set1 = {1, 2, 3, 4}
new_set2 = {3, 4, 5}

# delete element
# without error
# new_set1.discard(555555)

# with error
# new_set1.remove(5555555555)

# random elem
# element = new_set1.pop()
# print(element)
# print(new_set1)

#  common elements
common_ = new_set1 & new_set2
common = new_set1.intersection(new_set2)

print(common)

# union all
union_all_ = new_set1 | new_set2
union_all = new_set1.union(new_set2)
print(union_all)

# difference in two sets
diff_1 = new_set1 ^ new_set2


# difference presented in first but not in second
# diff_2 = new_set1.difference(new_set2)
diff_2 = new_set1 - new_set2

print(diff_2)

dict_from_set = dict.fromkeys(union_all, 555)
print(dict_from_set)


string_long = 'kjdsfhgjkdfkghdfkFFFFjhgdfjhsgjkldhfskjlghgkghkjldfghdfjg'
set_unique_chars = set(string_long)
dict_for_unique = dict.fromkeys(set_unique_chars, 0)
for elem in dict_for_unique:
    dict_for_unique[elem] = string_long.count(elem)

print(dict_for_unique)





