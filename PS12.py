
# 1. Prompt the user for number of items and load integers into a list
numbers = []

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    num = int(input(f"Enter integer #{i + 1}: "))
    numbers.append(num)

print("List:", numbers)

# 2. Insert 99 at position 1
numbers.insert(1, 99)
print("After inserting 99:", numbers)

# 3. Replace 99 with 100
index_99 = numbers.index(99)
numbers[index_99] = 100
print("After replacing 99 with 100:", numbers)

# 4. Create second list and extend first list
numbers2 = [500, 600, 700, 800, 900]
print("Second list:", numbers2)

numbers.extend(numbers2)
print("Extended first list:", numbers)

# 5. Remove value 800
numbers.remove(800)
print("After removing 800:", numbers)

# 6. Remove the third item
del numbers[2]
print("After removing third item:", numbers)

# 7. Create grades list
grades = ["A", "B", "C", "A", "A", "C"]

# 8. Count number of A grades
print("Number of A grades:", grades.count("A"))

# 9. Display index of first B grade
print("Index of first B grade:", grades.index("B"))

# 10. Look for F without generating an error
if "F" in grades:
    print("F is in the list")
else:
    print("F is not in the list")

# 11. Clear second list
numbers2.clear()
print("Second list after clear:", numbers2)

# 12. Delete second list and try to display it
del numbers2

try:
    print(numbers2)
except NameError:
    print("Error: numbers2 no longer exists")

# 13. Create players list
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print("Players list:", players)

# 14. Sort the players list
players.sort()
print("Sorted players list:", players)

# 15. Make a copy called players2
players2 = players.copy()
print("Players2:", players2)

# 16. Reverse players2
players2.reverse()

print("Players:", players)
print("Players2 reversed:", players2)