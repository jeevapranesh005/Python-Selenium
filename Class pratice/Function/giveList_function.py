

def increment(list2):
    for i in range(0,len(list2)):
        list2[i] +=5
    print(id(list))
        


list1=[10,20,30,40]
print(id(list1))
print(list1)
increment(list1)
print(id(list))
print(list1)