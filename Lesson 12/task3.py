def mini_calc(a, b, operation):
    try:
        float_a = float(a)
        float_b = float(b)
    except (ValueError, TypeError) as err:
        return err
    match operation:
        case "+":
            return float_a + float_b
        case "-":
            return float_a - float_b
        case "*":
            return float_a * float_b
        case "/":
            try:
                return float_a / float_b
            except ZeroDivisionError as err:
                return err
        case _:
            return "Operation must be: +, -, *, /"


print(mini_calc(5, 2, "-"))
print(mini_calc(5, 2, "45"))
print(mini_calc(5, "4B", "*"))
print(mini_calc(5, 0, "/"))
