# create a class with a class attribute a; create an object from it and set 'a' directly using object a=o. Does this change a class attribute?

class Demo:
    a = 10 # class attribute

o = Demo()
o.a = 0 # This creates an instance attribute, not changing the class attribute
print(Demo.a) # This will print 10
print(o.a) # This will print 0