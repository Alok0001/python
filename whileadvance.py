#using a while loop to continously prompt the user for input untill 'quit'
user_input = ''
while user_input != 'quit':
    user_input = input("enter a command (quit to exit): ")
    print("you entered",user_input)
    