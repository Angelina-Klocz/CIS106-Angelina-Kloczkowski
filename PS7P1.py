principle = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate: "))
year = 1
total_interest = 0
print("\nYear\tBeginning Balance\tEnding Balance")
while year <= 5:
   beginning_balance = principle
   interest = beginning_balance * (interest_rate / 100)
   ending_balance = beginning_balance + interest
   total_interest += interest
   print(f"{year}\t{beginning_balance:.2f}\t\t{ending_balance:.2f}")
   principle = ending_balance
   year += 1
print(f"\nTotal Interest Earned: $", format(total_interest,",.2f"))