class myclass:  # class

     
    #variable
    x=6

    def __init__(self,x):
        self.x=x
    
    #method
    def display(self):     # need to give atleast one parameter
        print("welcome my number  is",self.x)
    @staticmethod
    def display1():   
        print("welcome")

object=myclass(4)  # object


object.display()

print(object.x)
