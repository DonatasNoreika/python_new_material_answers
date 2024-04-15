a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
operation = input("Enter mathematical operation (+, -, *, /): ")

if operation == "+":
    result = a + b
    print(f"a + b = {result}")
if operation == "-":
    result = a - b
    print(f"a - b = {result}")
if operation == "*":
    result = a * b
    print(f"a * b = {result}")
if operation == "/":
    result = a / b
    print(f"a / b = {result}")
