str="abcXYZ784*&^def"


low =0
hig=0
non =0
for i in str:
    if(i>='a' and i<='z'):
        low +=1
    elif(i>='A' and i<='Z'):
        hig +=1
    else:
        non +=1

print("Lower case letters ",low)
print("Upper case letters ",hig)
print("Non - letters: ",non)
