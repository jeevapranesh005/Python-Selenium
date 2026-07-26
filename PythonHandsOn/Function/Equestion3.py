# Get the salary per month and hike from user 

def salHike(salary,hike):
    res = salary+(salary*hike/100)
    return res

salary = int(input("Enter the old salary : "))
Hike = int(input("Enter the HIKE : "))
result = salHike(salary,Hike)
print(result )