import pytest

from oop2 import SmartPhone, ButtonHomePhone
from practice import CurrentAccount, CreditAccount, Client


# @pytest.fixture(scope='function')
# @pytest.fixture(scope='class')
# @pytest.fixture(scope='module')
@pytest.fixture(scope='session')
def cell_phone() -> SmartPhone:
    instance = SmartPhone(price=556.00, brand='Apple', imei='jhg3565656565')
    return instance


@pytest.fixture(scope='function')
def button_phone() -> ButtonHomePhone:
    instance = ButtonHomePhone(price=50.00, brand='Apple')
    return instance


@pytest.fixture(scope='class')
def current_account() -> CurrentAccount:
    instance = CurrentAccount()
    return instance


@pytest.fixture(scope='class')
def credit_account() -> CreditAccount:
    instance = CreditAccount(limit=-2000)
    return instance

@pytest.fixture(scope='class')
def client() -> Client:
    instance = Client(name='Alex')
    return instance

@pytest.fixture(scope='class')
def another_client() -> Client:
    instance = Client(name='Bob')
    return instance