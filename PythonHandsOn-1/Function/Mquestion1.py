def sumOdd(low,high):
    sum =0
    for num in range(low,high+1):
        if(num%2!=0):
            sum =sum+num
       
    return sum

def sumEven(low,high):
    sum =0
    for num in range(low,high+1):
        if(num%2==0):
            sum =sum+num
       
    return sum




Oddsum =sumOdd(1,1000)
Evensum = sumEven(1,1000)
absolute = Oddsum-Evensum

print("The sum of odd numbers from 1 to 1000 is: ",Oddsum)
print("The sum of even numbers from 1 to 1000 is: ",Evensum)
print("The absolute difference between the two sums is: ",abs(absolute))