try:
    n = int(input("Enter the number : "))
    if n<=0:
        raise Exception("Enter positive number")
    tot=0
    for i in range(1,n+1):
        tot+=1/(i**i)
    print(round(tot,5))
except Exception as e:
    print(e)