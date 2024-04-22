def war_of_numbers(*args):
    even = []
    odd = []

    for arg in args:
        if arg % 2 == 0:
            even.append(arg)
        else:
            odd.append(arg)

    print(even, odd)
    sum_even = sum(even)
    sum_odd = sum(odd)

    if sum_even > sum_odd:
        difference = sum_even - sum_odd
        print(f"Even numbers wins! Difference: {difference}")
        return difference
    elif sum_even < sum_odd:
        difference = sum_odd - sum_even
        print(f"Odd numbers wins! Difference: {difference}")
        return difference
    else:
        print("It's draw!")


war_of_numbers(2, 8, 7, 5)
war_of_numbers(12, 90, 75)
war_of_numbers(5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243)
war_of_numbers(8, 7, 6, 5, 3, 2, 1)
