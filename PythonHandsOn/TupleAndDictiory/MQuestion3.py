test_list=[(4,5),(4,),(8,6,7),(1,),(3,4,6,7)]
k=3

res=[]

for i in test_list:
    if len(i)!=k:
        res.append(i)

print(res)