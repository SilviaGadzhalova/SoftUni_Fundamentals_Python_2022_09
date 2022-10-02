british_pounds = int(input())
us_dollars = british_pounds * 1.31
print(f"{us_dollars:.3f}")

# from forex_python.converter import CurrencyRates
#
# amount = int(input("Amount in GBP: "))
# c = CurrencyRates()
# current_rate = c.get_rate("GBP", "USD")
# result = amount * current_rate
# print(f"{amount} GBP is {result:.3f} USD")
