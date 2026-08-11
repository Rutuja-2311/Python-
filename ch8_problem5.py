'''
Write a python function to print first n lines of the following patterns:
***
**
*  for n = 3
'''

def pattern(n):
    if(n == 0):
        return 0
    print("*" * n)
    pattern(n - 1)


pattern(3)