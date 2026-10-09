# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The Vector is: {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The Vector is: {self.i}i + {self.j}j + {self.k}k")


# Example usage
v2 = TwoDVector(1, 2)
v2.show()
v3 = ThreeDVector(3, 4, 5)
v3.show()