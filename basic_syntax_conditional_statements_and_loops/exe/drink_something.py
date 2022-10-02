age = int(input())
drinks = ""
if age <= 14:
    drinks = "toddy"
elif 14 < age <= 18:
    drinks = "coke"
elif 18 < age <= 21:
    drinks = "beer"
else:
    drinks = "whisky"
print(f"drink {drinks}")