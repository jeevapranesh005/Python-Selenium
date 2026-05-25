def add(a,b):
    return a+b

def sub(a,b):
    return abs(a-b)

def mult(a,b):
    return (a*b)


def callback(operation, operand1,operand2):
    return operation(operand1,operand2)

val1 = int(input("Enter the 1st value : "))
val2=int(input("Enter the 2nd value : "))
choice =input("Enter the choice of add/subract/multiple : ")


if choice=="add":
    print(callback(add,val1,val2))

elif( choice=="subract"):
    print(callback(sub,val1,val2))
elif(choice=="multiple"):
    print(callback(mult,val1,val2))
else:
    print("give a correct operator")
