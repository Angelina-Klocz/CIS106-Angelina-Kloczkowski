#Get user input
last_name = input("Enter your last name: ")
dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: "))
#Calculate adjusted gross income
adjusted_gross_income = gross_income - (dependents * 12000)
#Determine tax rate
if adjusted_gross_income <= 50000:
  tax_rate = 0.20
else:
  tax_rate = 0.10
#Calculate income tax
income_tax = adjusted_gross_income * tax_rate
#Ensure minimum tax if negative
if income_tax < 0:
  income_tax = 100
#Display results
print("Last Name:", last_name)
print("Gross Income:", gross_income)
print("Number of Dependents:", dependents)
print("Adjusted Gross Income:", adjusted_gross_income)
print("Income Tax:", income_tax)
#End