#Get user input
books=int(input("Enter the number of books: "))
cost_per_book=float(input("Enter the cost per book: "))  
#Calculat order total
order_total=books*cost_per_book
if order_total>50:
    shipping_cost=0
else:
    shipping_cost=25
#Display results
print("\norder total: $",order_total)  
print("shipping cost: $",shipping_cost)
#End
