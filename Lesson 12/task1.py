# Function 1:
def is_positive(number: float | int | str) -> bool | ValueError | TypeError:
    try:
        float_number = float(number)
    except (ValueError, TypeError) as err:
        return err
    return float_number > 0


# print(is_positive(5))
# print(is_positive(-45.54))
# print(is_positive("45"))
# print(is_positive("45k"))
# print(type(is_positive({"45k": 5})))

# Function 2:
def concat_strings(*args: str, divider: str = " "):
    try:
        one_string = divider.join(args)
    except TypeError:
        return "Can concatenate only strings"
    except AttributeError:
        return "Divider must be a string"
    return one_string


# print(concat_strings("Code", "Academy", "Programming", "School"))
# print(concat_strings("Code", "Academy", "Programming", "School", divider=" | "))
# print(concat_strings("Code", "Academy", "Programming", "School"))


# Function 3:
def convert_to_number(text: str) -> float:
    try:
        return float(text)
    except ValueError:
        return "Conversion to number not possible"


# print(convert_to_number("4545"))
# print(convert_to_number("df54"))


# Function 4:
def add_numbers(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "Can only add numbers"


# print(add_numbers(5, 4))
# print(add_numbers(5, "5k"))


# Function 5:
def get_file_text(filename: str):
    try:
        with open(filename, 'r') as file:
            file_text = file.read()
    except FileNotFoundError as err:
        return err
    return file_text


# print(get_file_text("file.txt"))
# print(get_file_text("file2.txt"))


# Function 6:
import datetime


def plus_minus_days(year: int, month: int, day: int,
                    delta_days: int | float) -> datetime.datetime | ValueError | TypeError:
    try:
        date = datetime.datetime(year=year, month=month, day=day)
        new_date = date + datetime.timedelta(days=delta_days)
    except ValueError as err:
        return err
    except TypeError as err:
        return err
    return new_date

# print(plus_minus_days(2000, 12, 31, delta_days=5))
# print(plus_minus_days(2000, 12, 31, delta_days=-5))
# print(plus_minus_days(2000, 12, 31, delta_days="45"))
