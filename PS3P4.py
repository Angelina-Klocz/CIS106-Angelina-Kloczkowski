#PS3P4: Auto Discount
make= input("Enter the make of the car: ")
model= input("Enter the model of the car: ")
msrp= float(input("Enter the MSRP of the car: "))
discount_percent= float(input("Enter the discount percentage: "))
#Process
amount_off= msrp * discount_percent / 100
discount_price= msrp - amount_off
#Output
print("Make: ", make)
print("Model: ", model)
print("MSRP: $", format(msrp, ",.2f"))
print("Discount: ", discount_percent, "%")
print("Amount Off: $", format(amount_off, ",.2f"))
print("Discount Price: $", format(discount_price, ",.2f"))
