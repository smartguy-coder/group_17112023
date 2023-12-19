import json
from decimal import Decimal
from typing import Final

ENERGY_PRICE: Final = 2_500.36

# d = '{"age": 15, "weight": 50.5}'
# parsed = json.loads(d, parse_float=Decimal)
# print(parsed)


"""
    Написати функцію, яка розраховує розмір місячної оплати за теплопостачання з залежності від
    спожитої ерергії
    1Гка = 2500,36
"""


def calculate_month_heat_energy_cost(heat_volume: int | float) -> Decimal:
    """
    according to doc #35415-12/01/2022 OMR set energy price
    heat_volume - data from meter in Gcal (like 1.3689 or 26)
    """
    if heat_volume < 0:
        raise ValueError('Wrong data')

    result = heat_volume * ENERGY_PRICE
    final_result = Decimal(str(result)).quantize(Decimal('0.01'))
    return final_result

#
# cost = calculate_month_heat_energy_cost(3.36)
# print(cost)

"""
    Написати функцію, яка отримує на вхід список імен і повертає тільки унікальні імена
"""


def get_unique_names(names: list[str]) -> list[str]:
    # 1
    # processed_names = []
    # for name in names:
    #     processed_name = name.strip().title()
    #     if processed_name in processed_names:
    #         continue
    #     processed_names.append(processed_name)

    # 2
    processed_names = []
    for name in names:
        processed_name = name.strip().title()
        if processed_name not in processed_names:
            processed_names.append(processed_name)

    # 3
    # processed_names = [name.strip().title() for name in names] # not unique !!!
    # processed_names = [name.strip().title() for name in names if name != 'julia']  # not unique !!!
    # processed_names = {name.strip().title() for name in names}  # set !!!!!!!!!!
    return list(processed_names)
