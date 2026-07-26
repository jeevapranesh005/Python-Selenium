from numbers import Number
def multiply(a, b):
    try:
        if not isinstance(a, Number) or not isinstance(b, Number):
            raise TypeError
        return a * b
    except TypeError:
        print("Error: Invalid operand type!")
print(multiply(3, 4))
multiply("3", 4)
