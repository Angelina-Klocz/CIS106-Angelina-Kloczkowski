def compute_scores(s1, s2, s3):
    total = s1 + s2 + s3
    average = total / 3
    return total, average

name = input("Enter last name: ")
s1 = float(input("Enter score 1: "))
s2 = float(input("Enter score 2: "))
s3 = float(input("Enter score 3: "))
total, avg = compute_scores(s1, s2, s3)

print("Last Name:", name)
print("Total Points:", total)
print("Average Score:", avg)