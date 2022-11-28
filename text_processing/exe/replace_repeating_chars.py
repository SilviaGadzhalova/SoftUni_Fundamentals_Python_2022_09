starting_message = input()
final_message = ""
last_letter = ""
for current_letter in starting_message:
    if current_letter != last_letter:
        final_message += current_letter
        last_letter = current_letter
print(final_message)