#print("Hello! Last week!")

#Set
'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()

for i in students:
    if i["house"] not in houses:
        #houses.append(i["house"])
        houses.add(i["house"])

for h in sorted(houses):
    print(h)
'''

# Global Variables

'''
balance = 50
def main():
    print("Balance: ", balance)

if __name__ == "__main__":
    main()
'''

'''
balance = 10
def main():
    print("Balance: ", balance)
    deposite(100)
    withdraw(20)
    print("Balance: ", balance)

def deposite(n):
    global balance      # to edit global variable
    balance += n

def withdraw(n):
    global balance      # to edit global variable
    balance -= n

if __name__ == "__main__":
    main()
'''

'''
class Account:
    def __init__ (self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n
    
def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(20)
    print("Balance: ", account.balance)

if __name__ == "__main__":
    main()
'''

#Constants

'''
MEOWS =3

for _ in range(MEOWS):
    print("meow")
'''

'''
class Cat:
    MEOWS = 4

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
    
cat = Cat()
cat.meow()
'''

# Type Hints
# To run mypy, command -> python -m mypy filename.py
'''
def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("number: "))
meow(number)
'''

'''
def meow(n: int) -> None:       # "-> None" means the function return none as return value
    for _ in range(n):
        print("meow")

number: int = int(input("number: "))
meows: str = meow(number)
print(meow)
'''

'''
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("number: "))
meows: str = meow(number)
print(meows, end="")
'''

#Docstrings
'''
def meow(n: int) -> str:
    """
    Meow n times.
    :param n: number of times to meow
    :type n:int
    :raise TypeError: If n is not an int
    :return : A string of n meows, one per line
    :rtype : str
    """
    return "meow\n" * n

number: int = int(input("number: "))
meows: str = meow(number)
print(meows, end="")

'''

# argprase
'''
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py [-n NUMBER]")
'''
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

'''
'''
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
'''
'''
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
'''




































































































































