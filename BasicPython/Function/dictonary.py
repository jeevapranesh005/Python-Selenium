my_dicty={}
my_dict={1:"apple",2:"ball"}
my_dict={1:"cse","name":"ram","list":[1,2,3],"tuple":(10,20,30)}
print(my_dict[1])
print (type(my_dict[1]))
print (type(my_dict["list"]))
print (type(my_dict["tuple"]))
print(type(my_dict))



#creation dictory 
#1.using keyword
number=dict(x=5,y=0)
print(number)

#2.using mapping
number1=dict({'x':5,'y':1})
print(number1)

#3. using iteration
number2=dict([('x',5),('y',7)])
print(number2)


#dict into dict
myfamily ={"child1":{"name":"john","year":2004},
           "child2":{"name":"peter","year":2005}}
print(myfamily)
print(myfamily["child1"])
print(myfamily["child1"]["name"])
myfamily["child1"]["year"]=2026
print(myfamily["child1"])

#add new key pair
mydict= {"brand":"coco","item":"icecream","price":200}

mydict["color"]="red"
print(mydict)

#travesal
mydict= {"brand":"coco","item":"icecream","price":200}

for x in mydict:
    print(x,mydict[x])

#
        #keys and value
print(mydict.keys())
print(mydict.values())
print(mydict.items())  #list inside tuple

#
#pop(1)
#popitems()
d={1:"one",2:"two"}
d.popitem()
print(d)

#get
d={1:"one",2:"two"}

#update
d={1:"one",2:"two"}
d1={8:"hello"}
d.update(d1)
print(d)

#dict_compresion

dict={}
for x in range(11):
    

