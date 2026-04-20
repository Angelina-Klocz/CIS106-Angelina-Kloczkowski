def get_rate(job_code):
   if job_code.upper() == 'L':
       return 25
   elif job_code.upper() == 'A':
       return 30
   elif job_code.upper() == 'J':
       return 50
   else:
       return 0

def compute_pay(hours, rate):
  if hours > 40:
      overtime = hours - 40
      return (40 * rate) + (overtime * rate * 1.5)
  else:
      return hours * rate
    
def program4():
  total_gross = 0
  while True:
    choice = input("Do you want to enter employee data? (yes/no): ")
    if choice.lower() != "yes":
      break
    name =  input("Enter employee last name: ")
    job_code = input("Enter job code (L, A, J): ")
    hours = float(input("Enter hours worked: "))
    rate = get_rate(job_code)
    gross = compute_pay(hours, rate)
    total_gross =  total_gross + gross
    print("Employee Name: ", name)
    print("Gross Pay: $", gross)
  print("Total Gross Pay: $",total_gross)

program4()
