file = open("orders.txt", "r")
total_extended_price = 0
order_count = 0
while True:
  item = file.readline()
  if item == "":
    break
  quantity = int(file.readline().strip())
  price = float(file.readline().strip())
  extended_price = quantity * price
  total_extended_price += extended_price
  order_count  += 1
  print(item, quantity, price, extended_price)

average_order = total_extended_price / order_count
print("\nTotal extended price: ", total_extended_price)
print("Number of orders: ", order_count)
print("Average order: ", average_order)
file.close()