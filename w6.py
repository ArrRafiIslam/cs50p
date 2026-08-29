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

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    #print("hello,", line)
    print("hello,", line.rstrip())
























































































