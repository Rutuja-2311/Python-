while True:
    try:
        a = int(input("Hey, Enter a number: "))
    except ValueError as e:
        print("Please enter a valid integer.")
        print(e)
        
    else:
        print(a)
        print("I am inside else")
        break

print("Thank You")
