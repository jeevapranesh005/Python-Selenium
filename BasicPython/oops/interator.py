class ModOfTwo:

    def __init__(self, max_value=0):
        self.max = max_value

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):

        if self.n <= self.max:
            result = self.n % 2
            self.n += 1
            return result

        else:
            raise StopIteration


number = ModOfTwo(3)

i = iter(number)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))