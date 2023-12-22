first_number = 1
second_number = '0'

# if second_number:
#     print(first_number/second_number)
# else:
#     print(f'{second_number=}')

try:  # required
    result = first_number / second_number
except ZeroDivisionError: # if error in try
    result = 100
except TypeError as error:
    print(f'You have got an error {error=} {first_number=} {second_number=}')
    raise
else:  # if everything is ok in try
    print('No errors')
finally:  # works no matter what even before return
    print(9999999999999999999999999999999)
    result = 55
    print(f'{result=}')
#
# print(result)


def foo2():
    raise TimeoutError


def foo():
    try:
        result = 1 / 5
        n = foo2()
        return result
    except ZeroDivisionError:
        result = 100
    finally:
        print(888888888)
        result = 55

    return result

print(foo())


try:
    pass
    pass
    pass
    pass
    pass
    pass
except:
    pass











