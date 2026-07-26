from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        return "woof!"


class Cat(Animal):

    def make_sound(self):
        return "meow!"


# Object Creation
d = Dog()
c = Cat()





print(d.make_sound())
print(c.make_sound())