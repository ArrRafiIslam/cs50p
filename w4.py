# libraries
# random ---> 
# random.choice(sequence)
'''
import random

coin = random.choice(["heads","tails","again"])
print(coin)
'''
# from ---> from library_name import function_name
'''
from random import choice

coin = choice(["heads","tails","again"])
print(coin)
'''

# random.randint(a,b)
'''
import random

number = random.randint(1,10)
print(number)
'''

# random.shuffle(x)

'''
import random

cards=["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
'''

# statistics --->
# statistics.mean(x)
'''
import statistics

print(statistics.mean([100,94,83]))
'''

# command-line arguments --->
# sys.argv(x)
'''
import sys
print("hello, my name is", sys.argv[1])
'''
'''
import sys
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
'''

# sys.exit(statement)
'''
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
    #print("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    #print("Too many arguments")
#else:
    #print("hello, my name is", sys.argv[1])
print("hello, my name is", sys.argv[1])
'''

# Slice --->
'''
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
   
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)
'''


# Packages --->
# cowsay
'''
import cowsay
import sys

#if len(sys.argv) ==2:
    #cowsay.cow("hello, " + sys.argv[1])

if len(sys.argv) ==2:
    cowsay.trex("hello, " + sys.argv[1])
'''

# APIs
'''
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(response.json())
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])
'''

# Making my own library
'''
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello , {name}")

def goodbye(name):
    print(f"goodbye , {name}")

main()
'''
import sys
#from w4_p import hello
from w4_p import goodbye
if len(sys.argv) ==2:
    #hello(sys.argv[1])
    goodbye(sys.argv[1])
'''
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello , {name}")

def goodbye(name):
    print(f"goodbye , {name}")

main()
'''





































































































































































