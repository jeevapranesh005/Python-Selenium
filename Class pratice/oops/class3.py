# class method

class circle:

    def __init__(self, radious=1.0, color="red"):
        self._radious = radious
        self._color = color

    @classmethod
    def withradio(cls, radio):
        return cls(radio)
    
    

circle1 = circle.withradio(10)

print(circle1._radious)
print(circle1._color)