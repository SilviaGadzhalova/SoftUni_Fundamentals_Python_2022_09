from math import floor
string = input().split(">>")
total_tax_collected = 0
for car in string:
    vehicle = car.split()
    car_type = vehicle[0]
    year_for_taxing = int(vehicle[1])
    kilometres = int(vehicle[2])
    if car_type != "family" and car_type != "heavyDuty" and car_type != "sports":
        print("Invalid car type.")
        continue
    if car_type == "family":
        tax_year = 50
        total_tax_to_pay = floor(kilometres / 3000) * 12 + (tax_year - year_for_taxing * 5)
        print(f"A {car_type} car will pay {total_tax_to_pay:.2f} euros in taxes.")
        total_tax_collected += total_tax_to_pay
    elif car_type == "heavyDuty":
        tax_year = 80
        total_tax_to_pay = floor(kilometres / 9000) * 14 + (tax_year - year_for_taxing * 8)
        print(f"A {car_type} car will pay {total_tax_to_pay:.2f} euros in taxes.")
        total_tax_collected += total_tax_to_pay
    elif car_type == "sports":
        tax_year = 100
        total_tax_to_pay = floor(kilometres / 2000) * 18 + (tax_year - year_for_taxing * 9)
        print(f"A {car_type} car will pay {total_tax_to_pay:.2f} euros in taxes.")
        total_tax_collected += total_tax_to_pay

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
