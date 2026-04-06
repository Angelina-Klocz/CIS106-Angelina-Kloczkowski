response = input("Do you want to run the program? (Yes/No): ")
total_discounts = 0
while response == "Yes":
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))
    extended = quantity * price
    if extended > 10000:
        discount_rate = 0.25
    else:
        discount_rate = 0.10
    discount = extended * discount_rate
    total = extended - discount
    print("Extended Price:", extended)
    print("Discount:", discount)
    print("Total:", total)
    total_discounts = total_discounts + discount
    response = input("Do you want to enter another order? (Yes/No): ")
print("Total Discounts:", total_discounts)
