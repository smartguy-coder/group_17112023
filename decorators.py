from typing import Callable, Any

# n = print
# n(99999)


# def add_log(func: Callable, value: Any):
#     print(f"{func.__name__} {func(value)}")
#
#
# def worker(number: int):
#     return number * 3

# import dis
#
# print(dis.dis(worker))
#
#
# worker.count = 569
# #
# #
# #
# # add_log(n, 56566655)
# # add_log(worker, 56566655)
#
# print(worker.__dict__)

########################################################

def james_bond(func: Callable):
    def wrapper(*args, **kwargs):
        print(args)
        print(*args)
        print(kwargs)
        result = func(*args, **kwargs)
        print(func.__name__)
        float_result = float(result)
        print(float_result)
        print('spying.....')
        return float_result
    return wrapper


def mult_3(number: int) -> int:
    return number * 3


# power_number_to_number = james_bond(power_number_to_number)
@james_bond
def power_number_to_number(base: int, power: int) -> int:
    return base ** power


def mult_4(number: int) -> float:
    return number * 4.0


def get_number_str(number: int) -> str:
    return str(number) * 3

#
# mult_3 = james_bond(mult_3)
# mult_4 = james_bond(mult_4)
# get_number_str = james_bond(get_number_str)

# power_number_to_number = james_bond(power_number_to_number)
# print(mult_3)
# mult_3(5555555)
# mult_4(5555555)
# mult_4(25)
# mult_4(40)
data = power_number_to_number(power=9, base=5)
print(data)



