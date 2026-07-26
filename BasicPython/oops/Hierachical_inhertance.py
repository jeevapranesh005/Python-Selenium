class num:
    def __init__(self):
        self.x=20
        self.y=10

class add(num):
    def findsum(self):
        self.z=self.x+self.y
        print("sum is ",self.z)

class sub(num):
    def findsum(self):
        self.z=self.x-self.y
        print("sub is ",self.z)
    
obj = add()
obj.findsum()

obj2=sub()
obj2.findsum()