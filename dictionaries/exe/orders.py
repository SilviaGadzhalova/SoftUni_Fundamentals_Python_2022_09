product_dictionary = {}
while True:
    current_product = input()
    if current_product == "buy":
        break
    product, price, quantity = current_product.split()
    price = float(price)
    quantity = int(quantity)
    if product not in product_dictionary.keys():
        product_dictionary[product] = []
        product_dictionary[product].append(price)
        product_dictionary[product].append(quantity)
    else:
        if product_dictionary[product][0] != price:
            product_dictionary[product][0] = price
        product_dictionary[product][1] += quantity
for product_name, value in product_dictionary.items():
    total_price = float(value[0]) * int(value[1])
    print(f"{product_name} -> {total_price:.2f}")
