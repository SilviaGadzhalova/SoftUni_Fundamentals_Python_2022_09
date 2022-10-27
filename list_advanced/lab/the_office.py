nums = list(map(int, input().split()))
multiply_factor = int(input())
multiply_list = list(map(lambda x: x * multiply_factor, nums))
filtered_list = list(filter(lambda x: x >= sum(multiply_list) / len(multiply_list), multiply_list))
if len(filtered_list) >= len(multiply_list) / 2:
    print(f"Score: {len(filtered_list)}/{len(multiply_list)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_list)}/{len(multiply_list)}. Employees are not happy!")

