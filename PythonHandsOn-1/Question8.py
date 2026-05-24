rate = float(input("Average Rating : "))

dig = int(rate)

sub = float(rate-dig)

if(sub<0.5):
    print(dig)
else:
    print((dig+1))