qty = int(input("Enter the quantity of widgets: "))
if qty > 1000:
   price = 10
elif qty > 500:
   price = 20
else:
   price = 30
  
extended_price = qty * price
tax = extended_price * 0.07
total = extended_price + tax

print(f"Extended price: ${extended_price}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")
