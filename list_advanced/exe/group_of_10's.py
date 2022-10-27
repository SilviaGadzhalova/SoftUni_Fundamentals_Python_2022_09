numbers = [int(n) for n in input().split(", ")]
sorted_numbers = []

for number in range(1, 10 + 1):
    sorted_numbers.clear()
    if len(numbers) != 0:
        for num in numbers:
            if int(num) <= number * 10:
                sorted_numbers.append(num)
        for d in sorted_numbers:
            numbers.remove(d)

        print(f"Group of {number * 10}'s: {sorted_numbers}")


# numbers_sequence = list(map(int, input().split(", ")))
# max_group = max(numbers_sequence) // 10 + 1
# if max(numbers_sequence) % 10 == 0:
#     max_group -= 1
# current_group = 0
# for groups in range(max_group):
#     group_list = [number for number in numbers_sequence if current_group < number <= (current_group + 10)]
#     current_group += 10
#     print(f"Group of {current_group}'s: {group_list}")
#     group_list.clear()