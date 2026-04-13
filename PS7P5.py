file = open("students.txt", "r")
total_tuition = 0
student_count = 0
while True:
  last_name = file.readline()
  if not last_name:
    break
  last_name = last_name.strip()
  district_code = file.readline().strip()
  credits = int(file.readline().strip())
  credits = int(credits)
  if district_code == "I":
   cost_per_credit = 250
  else:
    cost_per_credot = 500
  tuition = credits * cost_per_credit
  total_tuition += tuition
  student_count += 1
  print("Student:", last_name)
  print("Credits:", credits)
  print("Tuition:", tuition)
file.close()
print("\nTotal Tuition", total_tuition)
print("Number of Students:", student_count)