from collections import Counter

lst=[(5,6),(1,2),(6,5),(9,1),(6,5),(2,1)]
c=Counter(lst)
ans=0

for i in c:
    if i[0]<i[1]:
        ans+=min(c[i],c[(i[1],i[0])])

print(ans)