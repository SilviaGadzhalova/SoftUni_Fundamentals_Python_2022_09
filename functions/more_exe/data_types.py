def result_number(type_d, num):
    if type_d == "int":
        return int(num) * 2
    elif type_d == "real":
        return f"{float(num) * 1.5:.2f}"
    elif type_d == "string":
        return f"${num}$"


data_type = input()
number = input()
print(result_number(data_type, number))
