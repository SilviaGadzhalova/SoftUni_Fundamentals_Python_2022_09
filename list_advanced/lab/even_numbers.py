nums = list(map(int, input().split(", ")))
index = [num for num in range(len(nums)) if nums[num] % 2 == 0]
print(index)
