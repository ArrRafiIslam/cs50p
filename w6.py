'''
names =[]
for _ in range(3):
    #names = input("Whats your name? ")
    names.append(input("Whats your name? "))
#print(f"hello, {name}")

for name in sorted(names):
    print(f"hello, {name}")
'''
# open a file 
'''
name = input("Whats your name? ")
#file = open("names.txt", "w")
file = open("names.txt", "a")
#file.write(name)
file.write(f"{name}\n")
file.close()
'''
# WITH syntax
'''
name = input("Whats your name? ")
#file = open("names.txt", "w")
with open("names.txt", "a") as file:
#file.write(name)
    file.write(f"{name}\n")
'''

# read
'''
with open("names.txt", "r") as file:
    #lines = file.readlines()
    for line in file:
        print("hello,", line.rstrip())

#for line in lines:
    #print("hello,", line)
    #print("hello,", line.rstrip())
'''
'''
names=[]
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

#for name in sorted(names):
for name in sorted(names, reverse = True):
    print(f"hello, {name}")
'''
'''
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
'''


# CSV
'''
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
'''

'''
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
'''

'''
students=[]
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for i in sorted(students):
    print(i)
'''

'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student ={}
        #student["name"] = name
        #student["house"] = house
        student = {"name": name, "house": house}
        students.append(student)

for i in students:
    print(f"{i['name']} is in {i['house']}")   
'''
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

def get_name(student):
    return student["name"]

for i in sorted(students, key = get_name):
    print(f"{i['name']} is in {i['house']}")

# times tamp 50:35
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for i in sorted(students, key =lambda i: i["name"]):
    print(f"{i['name']} is in {i['house']}")




















































































