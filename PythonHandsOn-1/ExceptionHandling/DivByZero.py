def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")


print(safe_division(10, 2))
safe_division(8, 0)
