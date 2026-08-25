# integer
#x=int(input("What is x?"))
#y=int(input("What is y?"))
#z= int(x) + int(y)
#print(x+y)

# floating point
#x=int(input("What is x?"))
#y=int(input("What is y?"))
#print(x+y)

# rounding number
#x=float(input("What is x?"))
#y=float(input("What is y?"))
#z = round (x+y)
#print(z)

# putting commas for speificng millons or billions etc
#print(f"{z:,}")

# division
#z = x/y
#print(z)

# rounding floating point by n digits
#z = round (x/y,2)
#print(f"{z:.2f}")

# function returning value
def main():
    x = int(input("What is X?"))
    print("X squred is", square(x))

def square(n):
    #return n*n
    #return n**2
    return pow(n,2)

main()


