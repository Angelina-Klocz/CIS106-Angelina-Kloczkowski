player_names = []
batting_avg = []
file = open("players.txt", "r")
for line in file:
    data = line.split()
    player_names.append(data[0])
    batting_avg.append(float(data[1]))
file.close()
def display_players(names, averages):
    print("Player Batting Averages:\n")
    for i in range(len(names)):
        print(names[i], "-", averages[i])
def search_player(names, averages, search_name):
    found = False
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print("\nPlayer Found:")
            print(names[i], "-", averages[i])
            found = True
    if found == False:
        print("Name not found")
display_players(player_names, batting_avg)
choice = "yes"
while choice == "yes":
    name = input("\nEnter player last name to search: ")
    search_player(player_names, batting_avg, name)
    choice = input("Search again? (yes/no): ").lower()