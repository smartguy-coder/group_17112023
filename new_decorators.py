from typing import Callable

ALLOW_PUBLIC = True

admins = [
    {'name': 'Alex', 'password': '1234'},
    {'name': 'Sam', 'password': '1379'},
]


def auth_dec(allow_public=False, file_name='logs.txt'):
    def wrapper1(func: Callable):
        def wrapper2(*args, **kwargs):
            if allow_public:
                result = func(*args, **kwargs)
                return {'data': result, 'status': 'ok', 'limit': len(result)}

            name = input('Enter your name >>> ')
            password = input('Enter your password >>> ')
            for admin in admins:
                if admin['name'] == name and admin['password'] == password:
                    result = func(*args, **kwargs)
                    return {'data': result, 'status': 'ok', 'limit': len(result)}
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(f'26122023;{name};{password}\n')
            return {'status': 'out of service'}
        return wrapper2
    return wrapper1


def get_not_secret_military_info() -> dict:
    return {'troops': 350_000, 'tanks': 5_000}


@auth_dec(allow_public=True, file_name='not_secret.txt')
def get_secret_military_info() -> dict:
    return {'russion_ship': 'Novocherkask', 'coord': (53.656, 42.89)}


@auth_dec(allow_public=False)
def get_secret_military_info_about_city(city: str) -> dict:
    return {'city': city, 'coord': (153.656, 42.89)}


data = get_secret_military_info_about_city(city='moscov')
data = get_secret_military_info_about_city(city='hhhh')
data = get_secret_military_info_about_city(city='ssssss')
print(data)
