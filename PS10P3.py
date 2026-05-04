def compute_sales(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    target = sales * 0.05
    return commission, target

name = input("Enter salesperson last name: ")
sales = float(input("Enter sales amount: "))

commission, target = compute_sales(sales)

print("Salesperson:", name)
print("Commission:", commission)
print("Next Year Target:", target)