f = open("ch9_file.txt")

print(f.read())

f.close()

# the same can be written using with statement like this:
with open("ch9_file.txt") as f:
    print(f.read())

# you dont have to explicitely close the file 
