''''Almost all books about programming languages start with a very simple program
that prints the text Hello, World! to the screen. Make such a program in Python.'''''

def hello_world(x):
    ''''Prints Hello, World! to the screen.'''''
    y = print(f"Hi {x}: Hello, World!")
    return y

x = input("Enter your name: ")
hello_world(x)

