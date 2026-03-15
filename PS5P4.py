tickets = int(input("Enter the number of tickets: "))

if tickets >= 25:
  price=50
elif tickets >=10:
  price=60
elif tickets >=5:
  price=70
else:
   price=75

total = tickets*price
print("Tickets:",tickets)
print(f"Price Per Ticket: ${price:.2f}")
print(f"Total Cost: ${total:.2f}")
print("Enjoy the show!")



        
