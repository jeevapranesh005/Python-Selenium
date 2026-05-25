geet="Wel12com"
dig=0
letter=0

for i in geet:
    if i.isnumeric():
        dig +=1
    elif i.isalpha():
        letter +=1
    else:
        pass

print("dig" ,dig)
print("letter ",letter)

