d1={'Gfg':20,'is':36,'best':100}
d2={'Gfg2':26,'is2':19,'best2':70}

v=list(d2.values())

res={}

for i,j in enumerate(d1.keys()):
    res[j]=v[i]

print(res)