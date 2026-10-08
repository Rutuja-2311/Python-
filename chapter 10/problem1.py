# Create a class "programmer"  for storing information of few programmers working at Microsoft.

from itertools import product


class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Rutuja", 120000, 1234)
print(p.name, p.salary, p.pin, p.company) # This will print the instance and class attributes
p = Programmer("Rohan", 150000, 5678)
print(p.name, p.salary, p.pin, p.company) # This will print the instance and class attributes

    