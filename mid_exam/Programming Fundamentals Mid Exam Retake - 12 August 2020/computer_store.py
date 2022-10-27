sum_without_tax = 0
special_command = False
while True:
    current_command = input()
    if current_command == "special":
        special_command = True
        break
    if current_command == "regular":
        break
    if float(current_command) < 0:
        print("Invalid price!")
        continue
    sum_without_tax += float(current_command)
total_taxes = sum_without_tax * 0.2
total_sum = sum_without_tax + total_taxes
if special_command == True:
    total_sum = total_sum - total_sum * 0.1
if total_sum == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_without_tax:.2f}$")
    print(f"Taxes: {total_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_sum:.2f}$")






