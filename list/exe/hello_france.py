item_price_list = input().split("|")
budget = float(input())

new_budget = 0  # Budget made of sold items.
profit = 0
current_item_price = 0  # The price for each item i have to buy.
spent_money_list = []  # The price of all bought items.
sold_items_price_list = []  # The prices of all bought items and after that sold with 40% increased price.

# Separate the Items and the Prices:
for items_price in item_price_list:
    items_price_split = items_price.split("->")
    item = items_price_split[0]
    price = float(items_price_split[1])

    # Check if the price is the price limit and Check if the budget is big enough to buy the item:
    if (item == "Clothes" and price > 50.00) \
            or (item == "Shoes" and price > 35.00) \
            or (item == "Accessories" and price > 20.50) \
            or (price > budget):
        continue
    budget -= price
    spent_money_list.append(price)
    price_item_sold = price * 1.4
    sold_items_price_list.append(price_item_sold)

profit = sum(sold_items_price_list) - sum(spent_money_list)
new_budget = sum(sold_items_price_list) + budget

[print(f"{sold_item:.2f}", end=' ') for sold_item in sold_items_price_list]
# for sold_item in sold_items_price_list:
#     print(f"{sold_item:.2f}", end=' ')
# print()
# if you use empty print() , you don't need to \n at the beginning of line 36
# empty print is used to make the program to go the next line after finishing the for loop, else it will print on the right side because of END
print(f"\nProfit: {profit:.2f}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")