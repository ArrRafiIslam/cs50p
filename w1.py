
"""
#compare
x = int(input("what is X?"))
y = int(input("what is y?"))

if x<y:
    print("X is less than Y")
elif x>y:
    print("X is greater than Y")
else:
    print("X is equal to Y")
"""


"""
#more than one argument
x = int(input("what is X?"))
y = int(input("what is y?"))

if x<y or x>y:
if x-2>0 and y-2>0:
if x !=y:
if x ==y:
    print(" equal")
else:
    print("X and Y are not greater than zero")
"""
"""
# grading
score = int(input("Score: "))
if  90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif  70 <= score < 80:
    print("Grade: C")
elif  60 <= score < 70:
    print("Grade: D")
elif  score>= 50:
    print("Grade: E")
else:
    print("Grade: F")
"""

'''
# modulo
x = int(input("What is X? "))

if x%2 == 0:
    print("even")
else:
    print("odd")
'''
'''
# parity function

def main():
    x = int(input("What is X? "))
    if is_even(x):
        print("even")
    else:
        print("odd")
"""
def is_even(n):
    if n%2 ==0:
        return True
    else:
        return False
"""
def is_even(n):
    #return True if n%2 ==0 else False
    return n%2 ==0 
main()    
'''


# match
'''
name = input("whats your name? ")
if name == "Harry":
    print("Gryffindor")
if name == "Ron":
    print("Gryffindor")
else:
    print("who?")
'''
'''
name = input("whats your name? ")
if name =="Harry" or name == "Ron":
    print("Gryffindor")
else:
    print("who?")
'''

'''
name = input("whats your name? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case _:
        print("Who?")
'''
name = input("whats your name? ")
match name:
    case "Harry" | "Ron":
        print("Gryffindor")
    case _:
        print("who?")








