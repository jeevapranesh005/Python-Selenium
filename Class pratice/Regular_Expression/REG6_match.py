import re

text = "Alan Turing was a pioneer of theroetical computer and science and artifical intelligence London"
res=re.search('computer',text)
print(res.group()) #search
print("start method = ",res.start())
print("end method = ",res.end())
print("span method = ",res.span() )
print("re attribute = ",res.re)  # output the pattern
print("string attribute = ",res.string)