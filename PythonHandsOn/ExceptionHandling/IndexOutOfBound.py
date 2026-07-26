def access_fifth_element(numbers):
    try:
        return numbers[4]
    except IndexError:
        print("Error: Index out of range!")
print(access_fifth_element([1, 2, 3, 4, 5, 6]))
access_fifth_element([1, 2, 3, 4])
