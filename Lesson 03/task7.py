nums = (87, 66, 45.85, 13, 66, 78, 66, 44, 2, 44)

# task 1:

print(sum(nums))

# task 2:

# 4502603482170394

sum = 1
for num in nums:
    sum *= num

print(sum)

# task 3:

print(max(nums))

# task 4:

words = ["My", "Love", "Is", "Coding"]

to_str = " ".join(words)
print(to_str)

# task 5:

list1 = ["one", 'two', 'three']
list2 = ["four", 'five', 'six']

result = list1 + list2
print(result)
