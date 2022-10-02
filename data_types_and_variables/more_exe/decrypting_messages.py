key = int(input())
number_of_lines = int(input())
message = ""
for letter in range(1, number_of_lines+1):
    letter = input()
    ascii_value = ord(letter) + key
    message += chr(ascii_value)
print(message)