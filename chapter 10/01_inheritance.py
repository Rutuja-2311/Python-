class Employee:
    company = "Google" # This is a class attribute
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.salary}")

#class Programmer:
#    company = "Microsoft" # This is a class attribute
#    def show(self):
#        print(f"The name of the programmer is {self.name} and the company is {self.salary}")

#    def showLanguage(self):
#        print(f"The name of the programmer is {self.name} and the language is {self.language}")

class Programmer(Employee): # This is a child class which inherits from the parent class Employee. The child class can access the attributes and methods of the parent class.
    company = "Microsoft" # This is a class attribute
    def showLanguage(self):
        print(f"The name of the programmer is {self.name} and the language is {self.language}")

a = Employee()
b = Programmer()

print(a.company, b.company) # This will print the class attributes of both classes. The child class can access the class attribute of the parent class.