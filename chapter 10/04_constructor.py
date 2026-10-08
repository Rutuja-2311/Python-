class Employee:
    language = "Python" # This is a class attribute
    salary = 50000

    def __init__(self, name, salary, language): #dunder method which is automatically called when an object is created. It is used to initialize the attributes of the class.
        self.name = name
        self.salary = salary
        self.language = language
        print("This is a constructor method. It is called when an object is created.")

    def getInfo(self):
        print(  f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")

harry = Employee("Harry", 120000, "JavaScript") # This will call the constructor method and print the message. The arguments passed to the constructor are not used in this case.
harry.name = "Harry" # This is an object/instance attribute
print(harry.name, harry.language, harry.salary) # This will print the instance and class attributes

