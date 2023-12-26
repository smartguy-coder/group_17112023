from datetime import datetime, timedelta
import time

ADDRESS = 'Hospital #5'


class Human:
    DNA = 'XXY'
    people = []

    def __init__(self, name: str, money: int = 0):
        self.name = name.title()
        self.money = money
        self.birthday = datetime.utcnow() - timedelta(seconds=5000)
        self.birth_place = ADDRESS
        self.DNA = 'YYX'
        self.people.append(self)

    @property
    def age(self):
        return (datetime.utcnow() - self.birthday).seconds

    def __del__(self):
        self.money = 0
        print(f'{self.name} все (((, {self.money}')

    def __str__(self) -> str:
        return f'{self.name} народився {self.birthday}'

    # def __repr__(self) -> str:
    #     return f'{self.name}'
    __repr__ = __str__

    def play_soccer(self):
        print(f'{self.name} is playing soccer')
        return self

    def sleep(self):
        print(f'{self.name} is sleeping')
        return self


alex = Human('alex', money=10000)
marta = Human('Marta')
print(alex)

Human.people.append(9999)
print(Human.people)

print(alex.money)
print(alex.name)
print(alex.birthday)
print(alex.people)
print(alex)
print(marta.__dict__)
alex.play_soccer().play_soccer().play_soccer()
marta.play_soccer().sleep()
print(alex.__dict__)
alex.money += 5000
print(alex.__dict__)
print(alex.age)
print(alex.age)



