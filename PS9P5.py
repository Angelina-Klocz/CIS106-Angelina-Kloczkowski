  percent = 0.70
    return value * percent
total_market = 0
total_assessed = 0

while input("Run program? (Yes/No): ").lower() == "yes":
    county = input("County: ")
    value = float(input("Market value: "))

    assessed = assessed_value(county, value)

    total_market += value
    total_assessed += assessed

    print("Assessed value:", assessed)

print("Total Market Value:", total_market)
print("Total Assessed Value:", total_assessed)