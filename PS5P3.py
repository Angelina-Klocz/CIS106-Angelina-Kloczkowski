principle = float(input("Enter the principal amount of CD: "))
years = int(input("Enter years to maturity of CD: "))

if principle > 100000 and years ==5:
  rate = 0.06
elif principle >= 50000 and principle <= 100000 and years == 10:
  rate = 0.05
elif principle >= 50000 and principle <= 100000 and years == 5:
  rate = 0.04
else:
  rate = 0.02
  
interest = principle * rate

print(f"Principle: ${principle:.2f}")
print(f"Interest Rate: {rate*100:.0f}%" )
print(f"First Year Interest: ${interest:.2f}")
