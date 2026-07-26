class Inputnotnum(Exception):
    pass
class divbyzero(Exception):
    pass
class invalidmul(Exception):
    pass

try:
    op = input("Operation : (+-*/)")
    try:
        a = float(input("Enter num 1 : "))
        b = float(input("Enter num 2 : "))
    except ValueError:
        raise Inputnotnum("Input must be integer")
    if op == "+":
        res = a+b
    elif op=="-":
        res = a-b
    elif op=="*":
        if a in (0, 1) or b in (0, 1):
            raise invalidmul("Cannot multiply by zero")
        res = a*b
    elif op=="/":
        if b==0:
            raise divbyzero("Division by zero is not allowed")
        res = a/b
        
    else:
        print("Invalid")
    print("res :",res )
        
except invalidmul as e:
    print("Error : ",e)
except Inputnotnum as e:
    print("Error : ",e)
except divbyzero as e:
    print("Error : ",e)