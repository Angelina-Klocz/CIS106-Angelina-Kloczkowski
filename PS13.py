class Employee:

    def __init__(self, first, last, pay, bonus_rate):
        self.first = first
        self.last = last
        self.pay = pay
        self.bonus_rate = bonus_rate

        self.email = first + "." + last + "@company.com"

    def calculate_bonus(self):
        return self.pay * self.bonus_rate

emp1 = Employee("John", "Smith", 50000, 0.10)
emp2 = Employee("Jane", "Doe", 60000, 0.15)

print("Employee 1")
print("Name:", emp1.first, emp1.last)
print("Email:", emp1.email)
print("Salary:", emp1.pay)
print("Bonus Amount:", emp1.calculate_bonus())

print()

print("Employee 2")
print("Name:", emp2.first, emp2.last)
print("Email:", emp2.email)
print("Salary:", emp2.pay)
print("Bonus Amount:", emp2.calculate_bonus())