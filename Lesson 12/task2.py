def division(a: int | float, b: int | float):
    try:
        result = a / b
    except ZeroDivisionError as err:
        return err
    except TypeError as err:
        return err
    else:
        return result
    finally:
        print("Attempted division")

# print(division(5, 2))
# print(division(25, 0))
# print(division(25, "0"))
