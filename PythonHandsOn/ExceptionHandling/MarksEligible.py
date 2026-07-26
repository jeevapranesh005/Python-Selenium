m = int(input("Enter the marks of maths : "))
p = int(input("Enter the marks of physics : "))
c= int(input("Enter the marks of chemistry : "))
tot=m+p+c
try:
    if m>=65 and p>=55 and c>=50 and tot>=180:
        print("Eligible")
    else:
        raise Exception("not eligible.")
except Exception as e:
    print("Exception : ",e)