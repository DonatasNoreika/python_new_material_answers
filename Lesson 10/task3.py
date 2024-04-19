def mini_calc(num1: int | float, num2: int | float) -> tuple[int | float, int | float, int | float, int | float]:
    return num1 + num2, num1 - num2, num1 / num2, num1 * num2


print(mini_calc(5, 2))
