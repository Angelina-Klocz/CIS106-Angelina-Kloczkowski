def compute_discount(qty, price, rate):
    total = qty * price
    discount = total * rate
    discounted_price = total - discount
    return discount, discounted_price
qty = float(input("Enter quantity: "))
price = float(input("Enter price: "))
rate = float(input("Enter discount rate (as decimal): "))
discount, final_price = compute_discount(qty, price, rate)

print("Quantity:", qty)
print("Price:", price)
print("Discount Amount:", discount)
print("Discounted Price:", final_price)
