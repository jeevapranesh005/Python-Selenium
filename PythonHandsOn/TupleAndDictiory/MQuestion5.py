words=["go","bat","me","eat","goal","boy","run"]
chars={'e','o','b','a','m','g','l'}

for i in words:
    if set(i)<=chars:
        print(i,end=" ")