str1 = '/*Jon is @developer & musician!!'

res=''
for i in str1:
    if((i>='a' and i<='z') or (  i>='A' and i<='Z')):
        res +=i
        
    else:
        res +='#'
print(res)