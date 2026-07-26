import re
text = "Alan Turing was a pioneer of theroetical computer and science and 4 artifical intelligence London"

res = re.search("Turing",text)
print(res)
print(res.span())