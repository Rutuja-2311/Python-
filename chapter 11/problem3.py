# Create a class 'Employee' and add salary and increment properties to it.

# Write a method 'SalaryAfterIncrement' method with a @property decorator with 
# a setter which changes the value of increment based on the salary.

class Employee:
    salary = 50000
    increment = 5000

    def show(self):
        print(f"Salary: {self.salary}")
        print(f"Increment: {self.increment}")

    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, new_increment):
        self.increment = new_increment

e = Employee()
e.show()
print(f"Salary after increment: {e.SalaryAfterIncrement}")
e.SalaryAfterIncrement = 6000
e.show()
print(f"Salary after increment: {e.SalaryAfterIncrement}")
