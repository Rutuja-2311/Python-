# create a class "pets" from a class "Animal" and further create a class "Dog" from "Pets". Add a method "Bark" in the "Dog" class.

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()  # Output: Bow Bow!