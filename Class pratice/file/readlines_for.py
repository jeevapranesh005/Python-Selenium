myobject = open("myfile.txt","w")
myobject.write("Hello everyo one , how are you\nki")

myobject.close()


myobject = open("myfile.txt","r")

data = myobject.readlines()

for line in data:
    print(line)

