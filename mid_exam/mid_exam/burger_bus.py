number_of_cities = int(input())
profit = 0
total_profit = 0
for city in range(1, number_of_cities + 1):
    name_of_the_city = input()
    owners_income = float(input())
    owners_expenses = float(input())
    profit = owners_income - owners_expenses
    if city % 3 == 0:
        profit -= owners_expenses * 0.5
    if city % 5 == 0:
        profit -= owners_income * 0.1
        if city % 3 == 0:
            profit += owners_expenses * 0.5
    total_profit += profit
    print(f"In {name_of_the_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
