grades = {"Tomas": 5, "Rokas": 9, "Laura": 10, "Donatas": 3, "Lukas": 2}

sum_grades = sum(grades.values())
len_grades = len(grades)
avg_grade = sum_grades / len_grades

print(avg_grade)

less_than_8 = {}
more_than_8 = {}

for name, grade in grades.items():
    if grade < 8:
        less_than_8[name] = grade
    else:
        more_than_8[name] = grade

less_than_8_students = set(less_than_8.keys())

print(less_than_8_students, more_than_8)

name = input("Enter student name: ")
if name in grades.keys():
    print(f"Student {name} found. Grade: {grades[name]}")
else:
    print("No student found")
