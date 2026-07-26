import re 
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"


email_text = "Contact us at trainner@gmail.in or Jeeva.pranesh@gmail.in"
email = re.findall(email_pattern,email_text)

if (email):
    print(email)
else:
    print("not foun")