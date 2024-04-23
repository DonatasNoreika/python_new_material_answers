class InvalidWeightException(Exception):
    pass


class InvalidHeightException(Exception):
    pass


def calculate_bmi(weight, height):
    if weight > 300:
        raise InvalidWeightException("Weight cannot exceed 300 kg.")
    if height > 2.5:
        raise InvalidHeightException("Height cannot exceed 2.5 meters.")
    return weight / (height ** 2)


try:
    print(calculate_bmi(301, 1.8))
except InvalidWeightException as e:
    print(e)
except InvalidHeightException as e:
    print(e)

try:
    print(calculate_bmi(80, 2.6))
except InvalidWeightException as e:
    print(e)
except InvalidHeightException as e:
    print(e)

try:
    print(calculate_bmi(80, 1.8))
except InvalidWeightException as e:
    print(e)
except InvalidHeightException as e:
    print(e)
