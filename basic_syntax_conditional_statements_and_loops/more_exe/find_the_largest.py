number = int(input())
str_number = str(number)
sorted_num = sorted(str_number, reverse = True)
final_str = ""
for i in range(len(str_number)):
    final_str += sorted_num[i]
print(int(final_str))