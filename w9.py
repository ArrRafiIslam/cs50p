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

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("number: "))
meow(number)












































































































































