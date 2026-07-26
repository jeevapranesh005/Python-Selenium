import re

patten = r"\b\w+ing\b"
text = "walking and talking is my activtit"

res= re.search(patten,text)
print(res)  #--> it return incude <.........class  ......>
print(res.group())  #--> it is use for return only the work 
res= re.findall(patten,text)

print(res)