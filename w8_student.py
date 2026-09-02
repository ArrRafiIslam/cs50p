#print("Hello, OOP!")
'''
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
'''

'''
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()
'''

'''
def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()
'''
#Tuple
'''
def main():
    #name, house = get_student()
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return name, house
    return (name, house)

if __name__ == "__main__":
    main()
'''
#List
'''
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return (name, house)
    return [name, house]

if __name__ == "__main__":
    main()
'''
#Dictionary
'''
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student={}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()
'''

'''
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    #student={}
    #student["name"] = input("Name: ")
    #student["house"] = input("House: ")
    #return student
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
'''

# Start of "CLASSES"
#class is a custom detatype
#when using class, it creates object/instance

'''
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")       #"name" and "house" are the "attributes"/"instance variables" of the class named "Student"

def get_student():
    student = Student()     #"student" is the "object"/"instance" of class named "Student"
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
'''

'''
class Student:
    #classes come with certain function/methods which are defineable and behave in a special way
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")       #"name" and "house" are the "attributes"/"instance variables" of the class named "Student"

def get_student():
    #student = Student()     #"student" is the "object"/"instance" of class named "Student"
    name = input("Name: ")
    house = input("House: ")
    student= Student(name, house)       #Constuctor call # Each class creates a functuion with the same name
    return student

if __name__ == "__main__":
    main()
'''
# raise

from multiprocessing import Value


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except ValueError:
        ...

if __name__ == "__main__":
    main()

# 59:17
































































































































































