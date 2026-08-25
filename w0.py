print("CS50P Lecture 0 - Functions")

# taking name as input and removing whitespace and capitalizing the first letter of the string
#name = input("What is your name?").strip().title()

# printing name as output
#print("hello, " + name)
#print("hello,", name)
#print(f"hello, {name}")

#  delete new line in print function by using end=""
#print("hello, ", end=" ")
#print(name)

# speerate between print function by using sep=""
#print("hello,", name, sep="...")

# removing whitespace from str
#name = name.strip()

# capitalize the first letter of the string
#name = name.capitalize()


# capitalize the first letter of each word in the string
#name = name.title()

# combine all the above functions
#name = name.strip().title()

# split user name into first and last name and print it
#first, last = name.split(" ")
#print(f"hello, {first} {last}")

# def / create new function
#def hello(to="world"):
    #print("hello", to)

#name = input("What is your name?")
#hello(name)
#print(name)
#hello()
#hello(name)

# main function calling
def main():
    name = input("What is your name?")
    hello(name)

def hello(to="world"):
    print("hello", to)

main()
