k=2

lst=[(2,3),(3,3),(1,4),(2,4),(2,5),(3,4),(1,4),(3,4),(4,7)]

d={}
res=[]

for i in lst:
    if d.get(i[0],0)<k:
        res.append(i)
        d[i[0]]=d.get(i[0],0)+1

print(res)