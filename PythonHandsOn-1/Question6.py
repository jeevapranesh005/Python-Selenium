weight =float(input("Weight: "))
Height =float(input("Height: "))
if(weight<0):
    print("The weight is negative")
elif(Height<0):
    print("Then Height is negative")
elif(Height<0 or weight<0):
    print("The height and weight is negative")
else:
    res=weight/(Height**2)
    print(f"BMI:{res:.2f}")