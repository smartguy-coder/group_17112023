from decimal import Decimal
import pytest

import library2


def test_energy_cost_2gcal():
    volume = 2
    expected = Decimal('5000.72')
    actual_result = library2.calculate_month_heat_energy_cost(volume)
    assert expected == actual_result


def test_energy_cost_1gcal():
    volume = 1
    expected = Decimal('2500.36')
    actual_result = library2.calculate_month_heat_energy_cost(volume)
    assert expected == actual_result


def test_energy_cost_minus_gcal():
    volume = -1
    with pytest.raises(ValueError):
        library2.calculate_month_heat_energy_cost(volume)


def test_energy_cost_0gcal():
    volume = 0
    expected = Decimal('0')
    actual_result = library2.calculate_month_heat_energy_cost(volume)
    assert expected == actual_result


def test_get_unique_names():
    income_data = ['alex', '          Alex', 'julia', 'john', '555']
    expected = ['Alex', 'Julia', 'John', '555']
    actual_result = library2.get_unique_names(income_data)
    assert expected == actual_result
