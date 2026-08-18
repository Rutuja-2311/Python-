# Repeat program 4 for a list of such words to be censored.

words = ["dog", "dress", "beach", "book"]

with open("ch9_file4.txt", "r", encoding="utf-8") as f:
    content = f.read()

for word in words:
   content = content.replace(word, "#" * len(word))

with open("ch9_file4.txt", "w", encoding="utf-8") as f:
    content = f.write(content)