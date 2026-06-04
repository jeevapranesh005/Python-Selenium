import re

text ="Alan Turing was born on 23 june 1912 Long in @ London."

res=re.findall(r"\AAlan",text)    #begging of String
res1=re.findall(r"on\b",text)      # end of a word
res1=re.findall(r"\bLon",text)    # begging of a word
res2=re.findall(r"\d",text)       #only see the digit
res3=re.findall(r"\D",text)        #only see non digitt
res4=re.findall(r"\s",text)     #only give the space
res5=re.findall(r"\S",text)    #non space
# \w--> a-z A-Z 0-9 _
#\W --> other than this..
res6=re.findall(r"\Bon",text)


print(res6)