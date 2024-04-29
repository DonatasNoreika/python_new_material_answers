class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def subtract(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError as err:
            return err
        else:
            return result


calc = Calculator()
print(calc.add(5, 6))
print(calc.divide(5, 6))
print(calc.multiply(5, 6))
print(calc.subtract(5, 6))
print(calc.subtract(5, 0))
