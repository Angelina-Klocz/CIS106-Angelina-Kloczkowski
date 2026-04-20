def compute_mpg(miles, gallons):
   if gallons == 0:
      return 0
   return miles / gallons
def program3():
  trip_count = 0
  while True:
    choice = input("Do you want to enter trip data? (yes/no): ")
    if choice.lower() != "yes":
       break
    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons of gas used: "))
    mpg = compute_mpg(miles, gallons)
    trip_count =+ 1
    print("City:", city)
    print("Miles: ", miles)
    print("MPG: ", round(mpg, 2))
  print("Total trips entered:", trip_count)
program3()