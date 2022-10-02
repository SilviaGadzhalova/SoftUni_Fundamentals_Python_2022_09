name = input()
while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    counter = len(name)
    if counter < 5:
        print(f"{name} goes to Gryffindor.")
    elif counter == 5:
        print(f"{name} goes to Slytherin.")
    elif counter == 6:
        print(f"{name} goes to Ravenclaw.")
    elif counter > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if name == "Welcome!":
    print("Welcome to Hogwarts.")