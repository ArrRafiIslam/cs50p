# syntax error
'''
print("hello, world)
'''

# run-time error / value error

try:
    x = int(input("What is X? "))
    print(f"x is {x}")
except ValueError:
    print( "X is not an integer")

    