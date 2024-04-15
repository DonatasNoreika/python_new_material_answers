name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if age >= 21:
    print(f"Welcome to Casino, {name} {last_name}")
else:
    print("Sorry, you can't enter Casino")
