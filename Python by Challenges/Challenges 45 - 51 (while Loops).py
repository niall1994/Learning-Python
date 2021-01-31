#Challenge 48
count = 0
test = "y"

while test == "y":
    name = input("Who would you like to invite? ")
    print(name, "has now been invited")
    count = count + 1
    test = input("Would you like to invite someone else? (y to continue!)")

print(count,"people will be attending the party", "\n")

#challenge 51
num_bottles = 10

while num_bottles > 0:
    print("There are",num_bottles,"green bottles hanging on the wall",num_bottles,"green bottles hanging on the wall, and if one green bottle should accidentally fall")
    test = int(input("How many green bottles are hanging on the wall? "))

    while test != num_bottles -1:
        test = int(input("Try again! "))

    num_bottles = num_bottles - 1
    
print("There are no more green bottles on the wall!")
    
    
