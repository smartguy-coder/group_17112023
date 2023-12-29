from abc import ABC, abstractmethod
import datetime
import random
from typing import Self


class Phone(ABC):
    def __init__(self, price: float, brand: str):
        self.price = price
        self.brand = brand
        self.created_at = datetime.datetime.utcnow()
        self.net_number = random.randint(100000000, 9999999999)

    def call(self, other: Self):
        self.dial()
        other.dial()
        print(f'{self.net_number} is calling to {other.net_number}')

    @abstractmethod
    def dial(self) -> dict:
        raise NotImplemented


class ButtonHomePhone(Phone):
    def dial(self) -> dict:
        print(f'{self.brand} {self.net_number} call to local ATC')
        return {'connected': True}


class SmartPhone(Phone):
    def __init__(self, price: float, brand: str, imei: str):
        super().__init__(price, brand)
        self.imei = imei

    def dial(self) -> dict:
        print(f'{self.brand} {self.net_number} call to the cell ATC')
        return {'connected': True}

    @staticmethod
    def take_photo():
        print("""
        ------********
        ---********
        """)

    @staticmethod
    def check_imei(imei: str) -> bool:
        return imei.startswith('123')


button_phone = ButtonHomePhone(price=55.00, brand='alcatel')
button_phone.dial()

cell_phone = SmartPhone(price=556.00, brand='Apple', imei='jhg3565656565')

# print( isinstance(button_phone, Phone))
# print( isinstance(cell_phone, Phone))
# print(type(cell_phone) is type(button_phone))
#
# print(isinstance(True, int))
# print(isinstance(False, int))
# print(isinstance(False, bool))
# print(True + True)
#
# cell_phone.take_photo()
#
#
# SmartPhone.take_photo()
# print(SmartPhone.check_imei('123'))
# print(cell_phone.check_imei('kldjjfhgjkdf'))

cell_phone.call(button_phone)

print(cell_phone.__dict__)
cell_phone.cover = 'AC/DC'
print(cell_phone.__dict__)
