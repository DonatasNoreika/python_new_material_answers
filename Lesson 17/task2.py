class Employee:
    def __init__(self, firstname, lastname):
        self.fullname = f"{firstname} {lastname}"
        self.email = f"{firstname}.{lastname}@company.com".lower()


emp1 = Employee("Donatas", "Noreika")
emp2 = Employee("Laura", "Radvilaitė")

print(emp1.fullname, emp1.email)
print(emp2.fullname, emp2.email)
