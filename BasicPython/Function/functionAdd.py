#function
def add_mul(a,b,c):
    res = (a+b)*c
    return res

val1=int(input("val1: "))
val2=int(input("Val2 : "))
val3= int(input("val3 : "))
result = add_mul(val1,val2,val3)
print("the result is ",result)