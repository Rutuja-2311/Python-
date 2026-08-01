# if the name of two freinds are same; what will happen to the program in problem 6?

d = {}

name = input("Enter Freinds name: ")
lang = input("Enter language name: ")

d.update({name: lang})

name = input("Enter Freinds name: ")
lang = input("Enter language name: ")

d.update({name: lang})

print(d)