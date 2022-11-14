force_book = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        user_is_part_of_the_force = False
        for value in force_book.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_book.keys():
                force_book[force_side] = []
                force_book[force_side].append(force_user)
            else:
                force_book[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for key, value in force_book.items():
            if force_user in value:
                force_book[key].pop(value.index(force_user))
                break
        if force_side not in force_book.keys():
            force_book[force_side] = []
            force_book[force_side].append(force_user)
        else:
            force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side in force_book.keys():
    if len(force_book[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(force_book[force_side])}")
        for user in force_book[force_side]:
            print(f"! {user}")