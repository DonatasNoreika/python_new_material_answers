numbers = []

for x in range(1, 11):
    number = int(input(f"Enter integer number {x}: "))
    numbers.append(number)

print(f"Sum: {sum(numbers)}, average: {sum(numbers) / len(numbers)}")

# Alternative:

total = 0

for x in range(1, 11):
    number = int(input(f"Enter integer number {x}: "))
    total += number

print(f"Sum: {total}, average: {total / 10}")
