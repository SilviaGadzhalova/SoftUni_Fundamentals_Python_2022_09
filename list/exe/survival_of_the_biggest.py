list_of_integers = input(). split()
number = int(input())
list_of_integers_as_digits = []
for element in list_of_integers:
    list_of_integers_as_digits.append(int(element))
for _ in range(number):
    list_of_integers_as_digits.remove(min(list_of_integers_as_digits))
max_number_list = []
for element in list_of_integers_as_digits:
   max_number_list.append(str(element))
print(', '.join(max_number_list))


numbers = [int(number) for number in input().split()]
numbers_to_remove = int(input())
for remove in range(numbers_to_remove):
    numbers.remove(min(numbers))
# [numbers.remove(min(numbers)) for number in range(numbers_to_remove)]
print(*numbers, sep=', ')