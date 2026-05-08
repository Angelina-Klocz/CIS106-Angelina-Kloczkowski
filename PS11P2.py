last_names = [
    "Smith", "Johnson", "Brown", "Davis", "Miller",
    "Wilson", "Moore", "Taylor", "Anderson", "Thomas"
]

scores = [88, 92, 75, 81, 95, 79, 84, 90, 87, 93]

def display_students(names, grades):
    print("Students and Scores:")

    for i in range(len(names)):
        print(names[i], "-", grades[i])

def display_students_reverse(names, grades):
    print("\nStudents in Reverse Order:")

    for i in range(len(names) - 1, -1, -1):
        print(names[i], "-", grades[i])

display_students(last_names, scores)
display_students_reverse(last_names, scores)