morse_code_dictionary = {'.-': "A", '-...': "B", '-.-.': "C",
              '-..': "D", '.': "E", '..-.': "F", '--.': "G",
              '....': "H", '..': "I", '.---': "J", '-.-': "K",
              '.-..': "L", '--': "M", '-.': "N", '---': "O",
              '.--.': "P", '--.-': "Q", '.-.': "R", '...': "S",
              '-': "T", '..-': "U", '...-': "V", '.--': "W",
              '-..-': "X", '-.--': "Y", '--..': "Z"}

text = input().split("|")

for symbol in text:
    symbol = symbol.strip()
    letters = symbol.split(" ")
    for letter in letters:
        print(morse_code_dictionary[letter], end="")
    print(" ", end="")