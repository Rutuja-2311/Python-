# write a program to find out the line number where python is present from question 6.

with open("ch9_log7.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("Python" in line):
       print(f"Yes Python is present, Line no: {lineno}")
       break
    lineno += 1

else:
    print("No Python is not present")