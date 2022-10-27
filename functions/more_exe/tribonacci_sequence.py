def tribonacci_numbers(number):
    first_num = 1
    second_num = 1
    third_num = 2
    tribonacci_list = [first_num]
    if number > 1:
        tribonacci_list.append(second_num)
    if number > 2:
        tribonacci_list.append(third_num)
    while len(tribonacci_list) < number:
        for i in range(number - 3):
            current_num = first_num + second_num + third_num
            first_num = second_num
            second_num = third_num
            third_num = current_num
            tribonacci_list.append(current_num)
    return tribonacci_list


count_of_numbers = int(input())
print(*tribonacci_numbers(count_of_numbers))