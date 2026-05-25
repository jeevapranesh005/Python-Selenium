def apprial(salary,rating):
    if(salary<=0 or rating<=0 and rating>10):
        print("Invalid Input")
    else:
        
        if(rating>=1 and rating<=4):
            per= salary*0.10
            salary= salary+per
            print(int(salary))
        elif (rating>=4.1 and rating<=7):
            per= salary*0.25
            salary= salary+per
            print(int(salary))
        elif(rating>=7.1 and rating<=10):
            per= salary*0.30
            salary= salary+per
            print(int(salary))
        else:
            print("Invalid Input")
    

salary = int(input("Enter the salary : "))
rating = float(input("Enter the rating : "))

apprial(salary,rating)