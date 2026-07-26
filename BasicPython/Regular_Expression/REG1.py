import re
text = "Alan Turing was a pioneer of theroetical computer and science and artifical intelligence London"

res= re.search("^Alan.*was",text)
if(res):
    print("We have match")
else:
    print("we dont have a match")

print(res)


