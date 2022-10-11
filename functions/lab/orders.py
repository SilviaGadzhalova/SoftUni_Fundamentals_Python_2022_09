def total_price(product, quantity):
    if product == "coffee":
        return f"{coffee * quantity:.2f}"
    elif product == "water":
        return f"{water * quantity:.2f}"
    elif product == "coke":
        return f"{coke * quantity:.2f}"
    elif product == "snacks":
        return f"{snacks * quantity:.2f}"


coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00
product = input()
quantity = int(input())
print(total_price(product, quantity))
