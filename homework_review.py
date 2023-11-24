age = input("Enter your age >> ")
age = int(age)

salary = input("Enter your month salary >> ")
salary = float(salary)

retirement_age = 65
pahen = retirement_age - age

exchange_rate = 37.3

money = pahen * 12 * salary / exchange_rate

print(money)
