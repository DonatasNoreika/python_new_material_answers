numbers = []

while True:
    number = input("Enter integer number: ")
    if not number:
        break
    numbers.append(int(number))

print(numbers)
print(f"Sum: {sum(numbers)}, average: {sum(numbers) / len(numbers)}")
