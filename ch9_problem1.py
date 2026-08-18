# Write a program to read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle'.

f = open("ch9_poem.txt")
content = f.read()
if("twinkle" in content):
    print("the word Twinkle is present in the content")

else:
    print("the word Twinkle is not present in the content")
  
f.close()