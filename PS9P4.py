def ticket_price(miles):
  if miles >= 30:
      return 12
  elif miles >= 20:
      return 10
  elif miles >= 10:
      return 8
  else:
      return 5
total = 0
while input("Run program? (Yes/No): ").lower() == "yes":
  name = input("Last name: ")
  miles = int(input("Miles from Downtown Chicago: "))
  price = ticket_price(miles)
  total += price
  print("Ticket price:", price)
print("Total ticket revenue:", total)