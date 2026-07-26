class student:
    def getStudent(self):
        self.__rollno = input("ENter the roll number: ")
        self.__name=input("ENter the name: ")
    def printStudentInfo(self):
        print("RoleNumber: ",self.__rollno,"Name: ",self.__name)

class mark(student):
    def getmarks(self):
        self.getStudent()
        self.__mark1=float(input("Enter mark of sub1 : "))
        self.__mark2=float(input("Enter mark of sub2 : "))
        self.__mark3=float(input("Enter mark of sub3 : "))

    def printmarks(self):
        print("Mark1: ",self.__mark1)
        print("Mark2: ",self.__mark2)
        print("Mark3: ",self.__mark3)

    def caclToMarks(self):
        return self.__mark1 + self.__mark2 +self.__mark3

class Result(mark):
    def getResult(self):
        self.getmarks()
        self.__total=self.caclToMarks()
    def putResult(self):
        self.printmarks()
        print("Totsl marks out of 300 : ",self.__total)

obj = Result()
obj.getResult()
obj.putResult()