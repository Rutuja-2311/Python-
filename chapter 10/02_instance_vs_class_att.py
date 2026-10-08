class Employee:
    language = "Python" # This is a class attribute
    salary = 50000

harry = Employee()
harry.language = "JavaScript" # This is an object/instance attribute
print(  harry.language, harry.salary)