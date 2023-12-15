import library


def main():
    raw_age: str = library.get_user_age()
    age: int = library.convert_str_into_int(raw_age)
    candies: int = library.generate_reward(
        base=age,
    )
    print(f'You get {candies} candies')


if __name__ == '__main__':
    main()
