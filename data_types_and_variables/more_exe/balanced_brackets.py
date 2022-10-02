number_of_lines = int(input())
opening_bracket = 0
closing_bracket = 0

for i in range(number_of_lines):
    current_n = input()
    if current_n == '(':
        opening_bracket += 1
    elif current_n == ')':
        closing_bracket += 1
    if abs(opening_bracket - closing_bracket) != 1 and abs(opening_bracket - closing_bracket) != 0:
        break
    if closing_bracket > opening_bracket:
        break

if opening_bracket == closing_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")