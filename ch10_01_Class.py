class Employee:
    #name = "John Doe"
    language = "Python" # This is a class attribute
    salary = 50000

John = Employee()
John.name = "John Doe" # This is an object/instance attribute
print( John.name, John.language, John.salary)

rohan = Employee()
rohan.name = "Rohan Das"
print( rohan.name, rohan.language, rohan.salary)

# Here name is object attribute & salary & language are class attributes. 
# So, if we change the value of salary or language, it will be reflected in all the objects of that class. 
# But if we change the value of name, it will only be reflected in that particular object.