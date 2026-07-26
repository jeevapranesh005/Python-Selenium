def speed(low, high):
    if(low>high):
        print("Provide valid input")
    else:

        for num in range(low,high+1):
            count=0
            for i in range(1,num+1):
                if(num%i==0):
                    count +=1
            if(count==2):
                print(num,end=" ")

speed(8,5)