#Get user input
item=input("Enter an item (A or B):")  
quantity=int(input("Enter the quantity:"))
#Determine unit price
if item=="A":
    unit_price=10.00
else:
    unit_price=20.00
#Calculate extended price
extended_price=unit_price*quantity
#Display results
print("\nItem:",item)    
print("Unit Price: $",unit_price)
print("Extended Price: $",format(extended_price,'.2f'))
#End
