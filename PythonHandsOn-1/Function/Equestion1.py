def sum (a):
    odd=0
    even=0
    for i in range(a):
        if(i%2==0):
            even= even+i
        else:
            odd=odd+i

    print ("sum of even number is", even)
    print("sum of odd number is ",odd)

sum(10)
