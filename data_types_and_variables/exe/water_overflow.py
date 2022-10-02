number_of_lines = int(input())
water_tank_capacity = 255
total_liters = 0
for lines in range(number_of_lines):
    current_liters = int(input())
    if water_tank_capacity - current_liters< 0:
        print("Insufficient capacity!")
        continue
    water_tank_capacity -= current_liters
    total_liters += current_liters
print(total_liters)



