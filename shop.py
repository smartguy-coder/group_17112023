import decimal

price = 146.23
str_price = str(price) * 2
print(str_price)

age = "12"
next_age = int(age) + 1
print(next_age)

weight = input("Enter weight >>> ")
print(weight.isdigit())
capasity = 2
brutto = float(weight) + capasity
print(brutto)


cottage_cheese_price = decimal.Decimal(str(price))
quantity = decimal.Decimal("0.263")

total_cost = cottage_cheese_price * quantity
final_cost = total_cost.quantize(decimal.Decimal("0.00"))
print(final_cost)
