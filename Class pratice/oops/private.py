class Student:
    def __init__(self):
        self.name="shone"    #public variable
        self.__age=39   #private variable
        self._course="python"    #protected variable
object=Student()
print(object.name)
print(object._course)
print(object.__age)