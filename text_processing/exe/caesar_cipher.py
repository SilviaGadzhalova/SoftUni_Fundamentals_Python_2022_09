string = input()
final_string = ""
for character in string:
    current_character = chr(ord(character)+3)
    final_string += current_character
print(final_string)