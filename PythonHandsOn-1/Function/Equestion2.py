#Write a function to find the prime numbers between 1 to 100.

def prime(a,b):
    for num in range(a,b+1):
        count=0
        for i in range(1,num+1):
            if(num%i==0):
                count=count+1
            
        if(count==2):
            print(num)

prime(2,9)


