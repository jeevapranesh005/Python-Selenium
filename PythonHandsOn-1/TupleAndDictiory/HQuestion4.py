k=3
s="paradox"

d={}

for i in range(26):
    d[chr(97+i)]=chr(122-i)

ans=s[:k-1]

for i in s[k-1:]:
    ans+=d[i]

print(ans)