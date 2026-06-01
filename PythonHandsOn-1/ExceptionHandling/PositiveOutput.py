def get_positive_integer(a):
    try:
        if a<0:
            raise ValueError("Error: Invalid input! Please enter a positive integer.")
        return a
    except ValueError as e:
        print(e)    