#Challenge 36
name = input("What is your name? ")
name_num = int(input("How many times would you like to display your name? "))

for i in range(0,name_num):
    print(name)

print("\n")

#challenge 38

name = input("What is your name? ")
name_num = int(input("How many times would you like to display your name? "))

for i in range(0,name_num):
    print("\n")
    for string in name:
        print(string)

print("\n")

#Challenge 44
num_people = int(input("How many people would you like to invite? "))

if num_people >= 10:
    print("Too many people!")
else:
    for i in range(0,num_people):
        name = input("Who would you like to invite? ")
        print(name,"Has been invited!")
    
