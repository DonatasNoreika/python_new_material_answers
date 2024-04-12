a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
numbers = [a, b, c]

print(max(numbers))

# Alternative:

nums = []

for x in range(3):
    number = int(input("Enter number: "))
    nums.append(number)

print(max(nums))