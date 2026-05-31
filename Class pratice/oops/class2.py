class circle:

    
    def __init__(self,radious=1.0,color="red"):
        self._radious=radious
        self._color=color
    
    def getradio(self):
        return self._radious
    def getcolor(self):
        return self._color

    def setRadious(self,radious):
        self._radious=radious

    def setColor(self,color):
        self._color=color

    def __str__(self):
        return f"the circle radio is {self._radious} and the color is {self._color}"
    
circle1=circle()
print(circle1.getradio())
print(circle1.getcolor())
    
    
circle2=circle(1111,"good")
print(circle2.getradio())
print(circle2.getcolor())

circle3=circle()
print(circle3.__str__())
     