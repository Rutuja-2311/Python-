def main():
    try:
        a = int(input("Hey, Enter a number: "))
    except Exception as e:
        print("Please enter a valid integer.")
        print(e)
        return
    else:
        print(a)
        print("I am inside else")
        return
        
    finally:
        print("This finally block always executes.")


main()
