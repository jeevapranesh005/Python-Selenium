num1 = int(input("Enter the lower number: "))
num2 = int(input("Enter the upper number: "))

print(f"The prime numbers between {num1} and {num2} are:")

for i in range(num1, num2 + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)