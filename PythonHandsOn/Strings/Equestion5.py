str1 = "KarTHik"
low =""
high=""

for i in str1:
    if(i>='a' and i<='z'):
        low = i+low
    else:
        high=i+high

res=low[::-1]+high[::-1]
print(res)