def forecast(month, sales):
    month = month.lower()

    if month in ["jan", "feb", "mar"]:
        percent = 0.10
    elif month in ["apr", "may", "jun"]:
        percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        percent = 0.20
    else:
        percent = 0.25
    return sales * (1 + percent)

while input("Run program? (Yes/No): ").lower() == "yes":
    name = input("Enter last name: ")
    month = input("Enter month: ")
    sales = float(input("Enter sales: "))
    result = forecast(month, sales)
    print("Next month's sales:", result)