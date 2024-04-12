name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"You were born in {2024 - age}")

# Version with datetime:

import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

now_year = datetime.date.today().year
born_year = now_year - age

print(f"You were born in {born_year}")
