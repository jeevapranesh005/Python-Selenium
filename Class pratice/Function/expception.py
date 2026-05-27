import traceback


try:
    a= int(input("Enter the val1 : "))
    b= int( input("Enter the val2 : "))
    c=a/b
    print(c)
except Exception as e:   #run if expction occur
   traceback.print_exc()
else:        #run if no expction (optional)
    print("no exeption occcure")
finally:   # always execute (optinal)
    print("execution is succsufull")
