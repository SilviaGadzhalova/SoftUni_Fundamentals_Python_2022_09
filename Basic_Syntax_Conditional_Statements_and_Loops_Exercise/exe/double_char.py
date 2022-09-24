string = input()
word = ""
while string != "End" :
    if string != "SoftUni":
        for letter in string:
            word += letter+letter
        print(word)
    string = input()
    word = ""
