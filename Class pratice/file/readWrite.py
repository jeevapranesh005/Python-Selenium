print("now reading the contents of the file")

text = input("enter the value: ")
name= input("enter the value: ")
myobject = open("myfile.txt","a")

myobject.writelines([text+"\n",name+"\n"])

myobject = open("myfile.txt","r")
myobject.seek(0)
data = myobject.readlines()

for i in data:
    word=i.split()
    print(word)
