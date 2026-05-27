def incrementlist(list2):
    list2=[1,2,3,4,5]
    for i in range(0,len(list2)):
        list2[i]+=5
    print(id(list2))
    print(list2)

list1 = [10,20,30,40,50]
print(id(list1))
print(list1)
incrementlist(list1)
