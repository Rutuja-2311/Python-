# Write a class vector representing a vector of n dimentions. overload the + and * operator which calculate the sum and the dot (.) product of them.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y      
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9) # same direction vector

print("v1 + v2 =", v1 + v2)  # Output: (5, 7, 9)
print("v1 . v2 =", v1 * v2)  # Output: 32

print("v1 + v3 =", v1 + v3)  # Output: (8, 10, 12)
print("v1 . v3 =", v1 * v3)  # Output: 50