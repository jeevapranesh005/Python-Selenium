try:
    n = int(input("Enter the num: "))
    if n < 1 or n > 100:
        raise Exception("Enter value between 1 to 100 : ")
    total = 0
    for i in range(1, n + 1):
        total += i * i
        print(total)
except Exception as e:
    print(e)