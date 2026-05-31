class vechicle :
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def show(self):
        print("Details:",self.name,self.color,self.price)

    def max_speed(self):
        print("vechile speed is 150")

    def change_gear(self):
        print("vechile change 6 gear")

class car(vechicle):
    def max_speed(self):
        super().max_speed()
        print("car max speed is 240")

    def change_gear(self):
        super().change_gear()
        print("carchange 7 gear")

car = car('car x1','red',20000)
car.show()
car.max_speed()
car.change_gear()

vechicle =vechicle("truck x1 ",'white',40000)
vechicle.show()
vechicle.max_speed()
vechicle.change_gear()  