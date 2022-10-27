phones_list = input().split(", ")
while True:
    current_command = input()
    if current_command == "End":
        break
    command_list = current_command.split(" - ")
    command = command_list[0]
    phone = command_list[1]
    if command == "Add":
        if phone in phones_list:
            continue
        else:
            phones_list.append(phone)
    elif command == "Remove":
        if phone in phones_list:
            phones_list.remove(phone)
        else:
            continue
    elif command == "Bonus phone":
        bonus_phones = phone.split(":")
        old_phone = bonus_phones[0]
        new_phone = bonus_phones[1]
        if old_phone in phones_list:
            index_old_phone = phones_list.index(old_phone)
            phones_list.insert(index_old_phone + 1, new_phone)
        else:
            continue
    elif command == "Last":
        if phone in phones_list:
            phones_list.append(phones_list.pop(phones_list.index(phone)))
        else:
            continue
print(", ".join(phones_list))
