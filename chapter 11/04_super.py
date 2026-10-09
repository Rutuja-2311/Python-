class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

#o = Employee()
#print(o.a) #Prints the a attribute of the Employee class
#print(o.b) #shows an error because the b attribute is not present in the Employee class

#o = Programmer()
#print(o.a, o.b) #Prints the a and b attributes of the Employee and Programmer classes respectively

o = Manager()
print(o.a, o.b, o.c) #Prints the a, b, and c attributes of the Employee, Programmer, and Manager classes respectively