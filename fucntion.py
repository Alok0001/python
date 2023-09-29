#using indentation in a fucntion
def greet(name):
    if len(name) > 5:
        print("hello", name)
        print("nice to meet you!")
    else:
        print("hi there,",name)
        print("short and sweet!")


#calling the function
greet("alice")
greet("vighya")