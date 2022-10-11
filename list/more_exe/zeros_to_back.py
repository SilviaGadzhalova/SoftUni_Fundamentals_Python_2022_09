string = input(). split(", ")
final_string = []
counter = 0
for element in string:
    if element != "0":
        final_string.append(int(element))
    elif element == "0":
        counter += 1
for i in range(counter):
    final_string.append(0)
print(final_string)