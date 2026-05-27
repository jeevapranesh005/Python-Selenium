list =[1,2,3,4,5,6]

while True:
    
    print ("the list is ",list)

    print("1.Append an element \n2.insert an element\n3.Append a list to the given list \n4.modify an existing element\n5.Delete an existing element from its position\n6.Delete an existing element with given value \n7.sort the list in assending order \n8. sort the list in descending order \n9.Display the list")

    choice = int(input("Enter the choice : "))
    if(choice==1):
        ele = int(input("enter the elemement: "))
        list.append(ele)
        print("the element is appended")
        print(list)
    elif(choice==2):
        pos = int(input("Enter the position"))
        ele = int(input("Enter the value"))
        list.insert(pos-1,ele)
        print("the element is inserted")
        print(list)
    elif(choice==3):
        new_list=[20,30,40]
        print(list+new_list)
    elif(choice==4):
        index= int(input("Enter the index :"))
        val = int(input("enter the value : "))
        list[index]=val
        print(list)
    elif(choice==5):
        index = int(input("enter the position : "))
        del list[index-1]
        print(list)
    elif(choice==6):
        index = int(input("enter the value : "))
        list.remove(index)
        print(list)
    elif(choice==7):
        list.sort()
        print(list)
    elif(choice==8):
        list.sort(reverse=True)
        print(list)
    elif(choice==9):
        print(list)
    else:
        break