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
'''
print("Hello again!")
'''

#Unpacking
'''
first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")
'''

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print(total(100, 50, 25), "Knuts")
'''

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")
'''

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")
'''

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print(total(galleons=100, sickles=50, knuts=25), "Knuts")
'''

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
'''

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")
'''

#args & kwargs
'''
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
'''

'''
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)
'''

'''
def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)
'''

#map
'''
def main():
    yell("This is CS50")

def yell(word):
    print(word.upper())

if __name__ == "__main__":
    main()
'''
'''
def main():
    yell(["This", "is", "CS50"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()
'''
'''
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()
'''
'''
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()
'''

#List Comprehensions
'''
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)

if __name__ == "__main__":
    main()
'''
'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = []
for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)
'''
'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

'''


#Filter
'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
'''
'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
'''


# Dictionary comprehensions
'''
students = ["Hermione", "Harry", "Ron"]
gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)
'''

'''
students = ["Hermione", "Harry", "Ron"]
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)
'''
'''
students = ["Hermione", "Harry", "Ron"]
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)
'''

#Enumerate
'''
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])
'''
'''
students = ["Hermione", "Harry", "Ron"]
for i, student in enumerate(students):
    print(i + 1, student)
'''

#Generators & Iterators
'''
n = int(input("What's n? "))
for i in range(n):
    print("🐑" * i)
'''
'''
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print("🐑" * i)

if __name__ == "__main__":
    main()
'''
'''
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    return "🐑" * n

if __name__ == "__main__":
    main()
'''

'''
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()
'''
'''
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()
'''


































































































