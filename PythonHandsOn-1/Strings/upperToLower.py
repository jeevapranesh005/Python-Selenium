str = input("Enter the string: ")
result = ""
for i in str:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()

print(result)
