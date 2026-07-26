import re

text = "Alan aTuringb was a pioneer of theroetical Turing computer and science and artifical intelligence London"

res= re.findall("Turing",text)
print(res)
