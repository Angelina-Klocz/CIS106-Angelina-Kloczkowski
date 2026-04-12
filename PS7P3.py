file = open("employees.txt", "r")
total_bonus = 0
while True:
  last_name = file.readline().strip()
  if last_name == "":
     break
  salary = float(file.readline().strip())
  if salary >= 100000:
    rate = 0.20
  elif salary >= 50000:
    rate = 0.15
  else:
    rate = 0.10
  bonus = salary * rate
  total_bonus += bonus
  print(last_name, "Salary: $", salary, "Bonus: $", bonus)
file.close()
print("\nTotal Bonus Paid: $", total_bonus)