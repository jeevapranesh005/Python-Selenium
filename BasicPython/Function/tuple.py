a =10,100,[1,4]
print(type(a))
print(type(a[2]))
print(type(a[2][0]))
print(a)


#creation of tuple

t=tuple("jeeva")
print(t)

#delete
#it is only able to delete full tuple not with particular

del t
print(t)


#travesal

#slice 


#modify  but both are different not same "t"
t=(1,2,3,4,5,6)
print(t)
print(id(t))
t=(100,)+t[1:]
print(t)
print(id(t))



#opertion
i=(1,2,3)
if(2 in i):
    print("yes")


#assingment
a,b=2+2,2+3
print(a,b)


add='modi@gmail.org'
print(type(add))
uname,domin= add.split('@')
print(uname)

#count
#-->

qout,rem=divmod(10,12)
print(qout)
print(rem)