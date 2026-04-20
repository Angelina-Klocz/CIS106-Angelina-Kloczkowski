def compute_average(hits, at_bats):
  if at_bats == 0:
      return 0
  return hits / at_bats
def program2():
  count = 0
  while True:
      choice = input("Do you want to enter player data? (yes/no): ")
      if choice.lower() != "yes":
          break
      name = input("Enter player's last name: ")
      hits = int(input("Enter hits: "))
      at_bats = int(input("Enter at bats: "))
      avg = compute_average(hits, at_bats)  
      count += 1
      print("Player:", name)
      print("Batting Average:", round(avg, 3))
  print("Total number of players:", count)
program2()