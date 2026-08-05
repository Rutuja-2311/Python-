# Write a program to find out whether a given post is talking about python or not.
post = input("Enter the post: ")

if("python".lower() in post.lower()):
    print("This post is about python")

else:
    print("This post is not about python")