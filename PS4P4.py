#Get user input
appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance: "))
#Determine warranty cost
if appliance_cost > 1000:
    warranty_cost = appliance_cost*0.10
else:
    warranty_cost = appliance_cost*0.05
#Calculate total cost
total_cost = appliance_cost + warranty_cost
#Display results 
print("Appliance Name:", appliance_name)
print("Appliance Cost: $", appliance_cost)
print("Warranty Cost: $", warranty_cost)
print("Total Cost: $", total_cost)
#End
