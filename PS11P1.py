last_names = [
    "Smith", "Johnson", "Brown", "Davis", "Miller",
    "Wilson", "Moore", "Taylor", "Anderson", "Thomas"
]

def display_names(names):
    print("Names:")
    for name in names:
        print(name)

def display_reverse(names):
    print("\nNames in Reverse Order:")
    for i in range(len(names) - 1, -1, -1):
        print(names[i])

display_names(last_names)
display_reverse(last_names)