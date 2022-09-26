budget = float(input())
price_flour_kg = float(input())
price_eggs_pack = price_flour_kg*0.75
price_milk_l = price_flour_kg + price_flour_kg*0.25
needed_eggs = 1
needed_flour = 1
needed_milk = 0.250
number_of_loaves = 0
colored_eggs = 0
money_left = 0
price_one_loave = price_flour_kg + price_eggs_pack + price_milk_l * needed_milk
while budget > price_one_loave:
      budget -= price_one_loave
      number_of_loaves += 1
      colored_eggs += 3
      if number_of_loaves % 3 == 0:
            colored_eggs -= number_of_loaves - 2

money_left = abs(budget)
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
