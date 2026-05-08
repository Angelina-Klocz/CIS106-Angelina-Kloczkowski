last_names = [
    "Smith", "Johnson", "Brown", "Davis", "Miller",
    "Wilson", "Moore", "Taylor", "Anderson", "Thomas"
]
scores = [88, 92, 75, 81, 95, 79, 84, 90, 87, 93]
def find_highest(names, grades):
    high_var = 0
    high_index = 0
    for i in range(len(grades)):
        if grades[i] > high_var:
            high_var = grades[i]
            high_index = i

    print("Highest Score:")
    print(names[high_index], "-", high_var)

def find_lowest(names, grades):
    low_var = 999
    low_index = 0

    for i in range(len(grades)):

        if grades[i] < low_var:
            low_var = grades[i]
            low_index = i

    print("Lowest Score:")
    print(names[low_index], "-", low_var)
find_highest(last_names, scores)
find_lowest(last_names, scores)