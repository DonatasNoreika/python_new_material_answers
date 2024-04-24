def get_prime_numbers(n: int):
    prime_numbers = []
    for number in range(2, n + 1):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


def get_fibonacci_numbers(n: int):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers


def get_sum_of_digits(n: int):
    return sum([int(digit) for digit in str(n)])
