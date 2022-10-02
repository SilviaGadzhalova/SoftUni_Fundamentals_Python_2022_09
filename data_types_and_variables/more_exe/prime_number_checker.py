number = int(input())
prime = True

for current_number in range(2, number):
    if number % current_number == 0:
        prime = False
print(prime)