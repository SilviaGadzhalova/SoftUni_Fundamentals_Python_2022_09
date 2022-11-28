starting_string = input()
for index in range(len(starting_string)):
    if starting_string[index] == ":" and index != len(starting_string) - 1:
        print(f":{starting_string[index + 1]}")
