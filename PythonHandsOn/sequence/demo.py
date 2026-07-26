
num =5
if(num>0):
    fac =1
    for i in range(1,num+1):
        fac =fac *i
    print("factorial ", fac)
elif(num==0):
    print("factorial is 0")
else:
    print("number is negative")