class Demo:

    def add(self, *numbers):
        print(sum(numbers))

obj = Demo()

obj.add(1,2)
obj.add(1,2,3)
obj.add(1,2,3,4)