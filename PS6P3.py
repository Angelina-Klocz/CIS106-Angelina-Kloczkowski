response = input("Do you want to run the program? (yes/no): ")

count = 0

while response=="Yes":
  last_name = input("Enter your last name: ")
  score1 = float(input("Enter exam score 1: "))
  score2 = float(input("Enter exam score 2: "))
  average = (score1 + score2) / 2
  print("Name:", last_name)
  print("Average score:", average)
  count=count+1
  response = input("Do you want to enter another student? (yes/no): ")
print("Total students:", count)
