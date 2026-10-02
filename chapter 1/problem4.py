# Write a python program to print the contents of a directory using the os module.

import os

# Specify the directory path
directory = "/New folder" 

# Print the contents of the directory
for item in os.listdir(directory):
    print(item)
