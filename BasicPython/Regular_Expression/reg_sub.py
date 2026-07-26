import re
text = "Alan Turing was a pioneer of theroetical computer and science and theroetical artifical intelligence London"

res = re.sub("theroetical","pratical",text)
print(res)