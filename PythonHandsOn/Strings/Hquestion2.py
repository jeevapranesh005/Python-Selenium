str1="Abc"
str2="Xyz"


list1=list(str1)
list2=list(str2)
strlen= len(str2)
for a,b in zip(list1,list2):
    print(a+b)