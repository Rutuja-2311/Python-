class Employee:
    company = "Google" # This is a class attribute
    name = "John" # This is a class attribute
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python" # This is a class attribute
    def printLanguages(self):
        print(f"The name of the coder is {self.name} and the language is {self.language}")
   


class Programmer(Employee, Coder): # This is a child class which inherits from the parent class Employee. The child class can access the attributes and methods of the parent class.
    company = "Microsoft" # This is a class attribute
    def showLanguage(self):
        print(f"The name of the programmer is {self.company} and the language is {self.language}")

a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()