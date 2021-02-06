#Challenge 96
data = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(data)

#Challenge 97
data = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("What row would you like: "))
column = int(input("What column would you like: "))
print(data[row][column])

#Challenge 98
data = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("What row would you like? "))
print(data[row])

to_add = int(input("What value would you like to add? "))
data[row].append(to_add)

print("Your new data is:",data[row])

#Column 99
data = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("What row would you like? "))
print(data[row])

col = int(input("Which column would you like displayed?"))
print(data[row][col])

change = input("Would you like to change this value? (Y/N)")

while change != "Y" and change != "N":
    change = input("I said Y or N! Try again: ")

if change == "Y":
    new_value = int(input("What new value would you like? "))
    data[row][col] = new_value

print("Your new data is", data[row])


#Challenge 100
data = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},
        "Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
        "Anne":{"N":5239,"S":4802,"E":5820,"W":1859},
        "Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}
print(data)

#Challenge 101
data = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},
        "Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
        "Anne":{"N":5239,"S":4802,"E":5820,"W":1859},
        "Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}

name = input("What name would you like? ")
region = input("What region would you like? ")
print("The data for salesperson,",name,"in region",region,"is",data[name][region])
change = input("Would you like to change this figure? (Y/N) ")

while change != "N" and change != "Y":
    change = input("I said Y or N! Try again: ")

if change == "Y":
    new_value = int(input("What new figure would you like? "))
    data[name][region] = new_value

print(data[name])

#Challenge 102
data = [[],[],[]]
for i in range(0,4):
    name = input("Please the enter the name: ")
    age = int(input("How old is this person: "))
    shoe_size = float(input("What is there shoe size? "))
    data[0].append(name)
    data[1].append(age)
    data[2].append(shoe_size)

name_to_display = input("Whos information would you like? ")
index_to_display = data[0].index(name_to_display)

print("Name",data[0][index_to_display])
print("Age",data[1][index_to_display])
print("Shoe Size",data[2][index_to_display])

# Challenge 103
data = [[],[],[]]
for i in range(0,4):
    name = input("Please the enter the name: ")
    age = int(input("How old is this person: "))
    shoe_size = float(input("What is there shoe size? "))
    data[0].append(name)
    data[1].append(age)
    data[2].append(shoe_size)

for j in range(0,4):
    print("Name:",data[0][j])
    print("Age:",data[1][j])

    

