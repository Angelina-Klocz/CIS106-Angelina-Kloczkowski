#PS3P1: Stock Investment
ticker=input("Enter the ticker symbol:")
shares=float(input("Enter the number of shares:"))
cost_per_share=float(input("Enter the cost per share:"))
#Process
amount_invested=shares*cost_per_share
#Output
print("Ticker Symbol:",ticker)
print("Amount Invested:",amount_invested)