def even_and_odd_numbers(numbers):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in numbers:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return sum_of_odd_digits, sum_of_even_digits


number = input()
sum_of_odd_digits, sum_of_even_digits = even_and_odd_numbers(number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
