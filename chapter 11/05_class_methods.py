class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"This class value of a is = {cls.a}")

e = Employee()
e . a = 45

e. show()