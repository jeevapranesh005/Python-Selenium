str = input("Enter the  string: ")
result = ""
for i in str:
    if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
        result += i
    elif i == " ":
        result += i
    else:
        result += "#"
print(result)
