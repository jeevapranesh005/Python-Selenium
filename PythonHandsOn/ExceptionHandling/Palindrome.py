try:
    number = int(input("enter value: "))
    if str(number) == str(number)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
except ValueError:
    print("Enter only integer numbers")
