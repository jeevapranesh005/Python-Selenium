try:
    num = -9
    if(num<=0):
        raise ValueError("This is a negative error")
except ValueError as e :
    print(e)
print("Iam successfully handle")

