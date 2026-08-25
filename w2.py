

# while loop

"""
i = 3
while i!=0:
    print("meow")
    i = i-1
"""
"""
i = 1
while i<=3:
    print("meow")
    i = i+1
"""
"""
i =0
while i<3:
    print("meow")
    i +=1

"""


# for loops

'''
for i in [0,1,2]:
    print("meow")
'''
'''
for i in range(3):
    print("meow")
'''
'''
for _ in range(3):   # _ works same as i
    print("meow")
    print(_)
'''
'''
print("meow\n" * 3, end="")
'''

# user input for loop
"""
while True:
    n = int(input("What is n? "))
    '''
    if n<0:
        continue
    else:
        break
    '''
    if n>0:
        break

for _ in range(n):
    print("meow")
"""
'''
def main():
    meow(get_number())

def get_number():
    while True:
        n= int(input("what is n? "))
        if n>0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

'''

"""
# list in python

students = ["Hermione", "Harry", "Ron"]
'''
print(students[0])
print(students[1])
print(students[2])
'''
'''
for student in students:
    print(student)
'''
'''
for s in students:
    print(s)
'''

"""

'''
# length
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i+1,students[i])

'''


# dictionaries in python

'''
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
'''

students={
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
'''
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
'''

for s in students:
    print(s, students[s])

# video stamp 54:20













