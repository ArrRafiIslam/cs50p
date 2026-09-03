# syntax error
'''
print("hello, world)
'''

# run time errors
# value error 
'''
try:
    x = int(input("What is X? "))
    print(f"x is {x}")
except ValueError:
    print( "X is not an integer")

'''
# name error
'''
try:
    x = int(input("What is X? "))
    # print(f"x is {x}")
except ValueError:
    print( "X is not an integer")
# print(f"x is {x}")
else:
    print(f"x is {x}")
'''
'''
while True:
    try:
        x = int(input("What is X? "))
    except ValueError:
        print( "X is not an integer")
    else:
        # print(f"x is {x}")
        break

print(f"x is {x}")
'''

# create a fn to get integer
'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is X? "))
        except ValueError:
            print( "X is not an integer")
        else:
            # print(f"x is {x}")
            # break
            return x
main()
'''
'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            # x = int(input("What is X? "))
            return int(input("What is X? "))
        except ValueError:
            print( "X is not an integer")
        #else:
            # print(f"x is {x}")
            # break
            #return x
main()
'''


# finding error but passing it/ doing nothing with it using 'pass'
'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            # x = int(input("What is X? "))
            return int(input("What is X? "))
        except ValueError:
            pass
            #print( "X is not an integer")
        #else:
            # print(f"x is {x}")
            # break
            #return x
main()
'''

'''
def main():
    x = get_int("What is x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            # x = int(input("What is X? "))
            return int(input(prompt))
        except ValueError:
            pass
            #print( "X is not an integer")
        #else:
            # print(f"x is {x}")
            # break
            #return x
main()

'''


















































































































































































































































































































































































