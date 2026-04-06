response = input("Do you want to run the program? (Yes/No): ")
total_pay = 0
count = 0
while response == "Yes":
    last_name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    if hours > 40:
        overtime = hours - 40
        gross = (40 * rate) + (overtime * rate * 1.5)
    else:
        gross = hours * rate
    print("Employee:", last_name)
    print("Gross Pay:", gross)
    total_pay = total_pay + gross
    count = count + 1
    response = input("Do you want to enter another employee? (Yes/No): ")
if count > 0:
    average = total_pay / count
else:
    average = 0
print("Total Pay:", total_pay)
print("Number of Employees:", count)
print("Average Pay:", average)
