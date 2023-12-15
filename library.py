import constants


def get_four() -> int | float:
    result = 2 + 2.0
    return result


def get_simple_string() -> str:
    return '555'


def get_admin_name() -> str:
    return 'Alex'


# is are has should can
def is_string_from_digits(my_string: str) -> bool:
    has_string_only_digits = my_string.isdigit()
    return has_string_only_digits


def get_user_age() -> str:
    """only positive age in string format"""
    while True:
        user_input = input(constants.MSG_USER_INPUT).lstrip('0')
        if is_string_from_digits(user_input):
            return user_input
        print(constants.MSG_NOT_NUMERIC_INPUT)


def convert_str_into_int(number_string: str) -> int:
    is_convertable = is_string_from_digits(number_string.replace('.', ''))
    if not is_convertable:
        raise ValueError(f'Damn, cannot process {number_string} into number <from convert_str_into_int>')

    converted_value = float(number_string)
    converted_value = int(converted_value)
    return converted_value


def generate_reward(*, base: int | float, rise: int | float = 2) -> int:
    reward = int(base * rise)
    return reward
