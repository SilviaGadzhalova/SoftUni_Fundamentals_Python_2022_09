def calculation_func(a, b, operators):
    if operators == "multiply":
        return a * b
    elif operators == "divide":
        return int(a / b)
    elif operators == "add":
        return a + b
    elif operators == "subtract":
        return a - b


operators = input()
first_num = int(input())
second_num = int(input())
print(calculation_func(first_num, second_num, operators))
