quantity_food = float(input())*1000
quantity_hay = float(input())*1000
quantity_cover = float(input())*1000
guineas_weight = float(input())*1000
month_food = quantity_food
month_hay = quantity_hay
month_cover = quantity_cover
status = False
for day in range(1, 31):
    month_food -= 300
    if month_food <= 0 or month_hay <= 0 or month_cover <= 0:
        print("Merry must go to the pet store!")
        status = True
        break
    if day % 2 == 0:
        month_hay -= month_food * 0.05
    if day % 3 == 0:
        month_cover -= guineas_weight / 3

if not status:
    print(f"Everything is fine! Puppy is happy! Food: {month_food/1000:.2f}, Hay: {month_hay/1000:.2f}, Cover: {month_cover/1000:.2f}.")
