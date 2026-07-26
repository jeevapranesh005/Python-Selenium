def large(t,n):
    if n==1:
        return t[0]
    return max(t[n-1],large(t,n-1))

t=(11,65,54,23,76,33,82,98)
print(large(t,len(t)))