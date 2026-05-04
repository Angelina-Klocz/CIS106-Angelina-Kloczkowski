def compute_bowling(s1, s2, s3, handicap):
    avg = (s1 + s2 + s3) / 3
    avg_with_handicap = avg + handicap
    return avg, avg_with_handicap
name = input("Enter bowler last name: ")
s1 = int(input("Enter game 1 score: "))
s2 = int(input("Enter game 2 score: "))
s3 = int(input("Enter game 3 score: "))
handicap = int(input("Enter handicap: "))

avg, avg_h = compute_bowling(s1, s2, s3, handicap)

print("Bowler:", name)
print("Average Score:", avg)
print("Average with Handicap:", avg_h)