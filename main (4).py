#Get user input
quantity= int(input("Enter the quantity of item: "))  
#Determine unit price
if quantity > 1000:
    unit_price = 3.00
else:
    unit_price = 5.00
#Calculate extended price, tax, and total
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax
#Display the results
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
#End

    