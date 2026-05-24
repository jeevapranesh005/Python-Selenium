num = int(input("Enter the value"))

i = 1
sum = 0
while i <= num:
    num1 = int(input("val :"))

    if num1 < 0:
        break
    else:
        sum = sum + num1
        i = i + 1
print("the sum is ", sum)
