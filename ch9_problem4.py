'''
A file contains a word "Donkey" multiple times. you need to write a 
program which replace this word ##### by updating the same file.
'''

word = "Donkey"

with open("ch9_file4.txt", "r", encoding="utf-8") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("ch9_file4.txt", "w", encoding="utf-8") as f:
    content = f.write(contentNew)