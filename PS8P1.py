def compute_total(quantity, price):
  total = quantity * price
  if total > 10000:
    total *= 0.9
  return total

def program1():
  total_sum = 0
  
  while True:
    choice = input("Do you want to enter new data?     (yes/no): ")
    if choice.lower() != "yes":
      break
      
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))
    
    total = compute_total(quantity, price)
    total_sum = total_sum + total
    
    print("Quantity:",quantity)
    print("Price:",price)
    print("Total:",total)
    print("Sum of all totals:",total_sum)
program1()