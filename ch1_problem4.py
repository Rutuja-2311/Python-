import os

# Specify the directory path
directory = "/New folder" 

# Print the contents of the directory
for item in os.listdir(directory):
    print(item)
