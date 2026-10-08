class Employee:
    language = "Python" # This is a class attribute
    salary = 50000

    def getInfo(self):
        print(  f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")

harry = Employee()
#harry.language = "JavaScript" # This is an object/instance attribute
harry.getInfo()
#Empoyee.getInfo(harry) # This is also valid. We can call the method using the class name and passing the object as an argument.
harry.greet()