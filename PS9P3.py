def final_price(make, model, ev, msrp):
    make = make.lower()
    model = model.lower()
    ev = ev.lower()
    if ev == "y":
        percent = 0.30
    elif make == "honda" and model == "accord":
        percent = 0.10
    elif make == "toyota" and model == "rav4":
        percent = 0.15
    else:
        percent = 0.05
    discounted = msrp * (1 - percent)
    total = discounted * 1.07
    return total
total_msrp = 0
total_sales = 0
while input("Run program? (Yes/No): ").lower() == "yes":
    make = input("Make: ")
    model = input("Model: ")
    ev = input("Electric (Y/N): ")
    msrp = float(input("MSRP: "))
    price = final_price(make, model, ev, msrp)
    total_msrp += msrp
    total_sales += price
    print("Final price:", price)
print("Total MSRP:", total_msrp)
print("Total Sales:", total_sales)