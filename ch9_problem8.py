# write a program to make a copy of a text file "this.txt".

with open("ch9_this8.txt") as f:
    content = f.read()

with open("ch9_this8_copy.txt", "w") as f:
    f.write(content)