import datetime


# Function 1:
def sum_two_nums(num1: int | float, num2: int | float) -> int | float:
    """
    Function returns sum of num1 and num2

    :param num1: int or float number
    :param num2: int or float number
    :return: sum of num1 and sum2
    """
    return num1 + num2


print(sum_two_nums(5, 2))


# Function 2:
def get_square(num: int) -> int:
    return num ** 2


print(get_square(3))


# Function 3:
def concat_strings(strings: list[str], divider: str = " "):
    return divider.join(strings)


words = ["Good", "Morning", "World"]

print(concat_strings(words))


# Function 4:
def print_greeting(name: str = "World", qty: int = 1) -> None:
    for x in range(qty):
        print(f"Hello {name}!")


print_greeting()
print_greeting("Donatas")
print_greeting(qty=3)
print_greeting("Donatas", 3)


# Function 5:
def print_date_time() -> None:
    now = datetime.datetime.today()
    print(f"Today is: {now.year} year, {now.month} month, {now.day} day. Time: {now.time()}")


print_date_time()
