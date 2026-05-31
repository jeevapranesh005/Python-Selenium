class Complex:

    def __init__(self, r, i):
        self.real = r
        self.img = i

    
    def __add__(self, sec):
        r = self.real + sec.real
        i = self.img + sec.img
        return Complex(r, i)

    def __str__(self):
        return f"{self.real} + {self.img}i"


c1 = Complex(2, 3)
c2 = Complex(4, 5)

c3 = c1 + c2

print(c3)