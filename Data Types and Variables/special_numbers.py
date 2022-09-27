number = int(input())

for current_number in range(1, number+1):
    sum = 0
    digits = current_number
    while digits > 0:
        sum += digits % 10
        digits = int(digits / 10)
    if (sum == 5) or (sum == 7) or (sum == 11):
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")

# range_number = int(input())
# for number in range(1, range_number + 1):
#     status = False
#     sum_of_digits = 0
#     digits = number
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits / 10)
#     if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
#         status = True
#     print(f"{number} -> {status}")

# range_number = int(input())
# for number in range(1, range_number + 1):
#     number_string = str(number)
#     status = False
#     sum_numbers = 0
#     for character in number_string:
#         sum_numbers += int(character)
#     if sum_numbers in [5, 7, 11]:
#         status = True
#     print(f"{number} -> {status}")
