def compute_tuition(credits, district_code):
  if district_code.upper() == 'I':
    rate = 250
  elif district_code.upper() == 'O':
    rate = 550
  else:
    rate = 0
  return credits * rate

def program5():
  total_tuition = 0
  while True:
    choice = input("Do you want to enter student data? (yes/no): ")
    if choice.lower() != 'yes':
      break
    name = input("Enter student last name: ")
    credits = int(input("Enter number of credit hours: "))
    code = input("Enter district code (I/O): ")
    tuition = compute_tuition(credits, code)
    total_tuition = total_tuition + tuition
    print("Student: ", name)
    print("Tuition Owed: $", tuition)
  print("Total tuition owed by all students: $", total_tuition)

program5()
  