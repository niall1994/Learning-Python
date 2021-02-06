#Requires Libraries
from array import *
import random as rand

#Challenge 88
nums = array('i',[])

for i in range(0,4):
    number = int(input("Enter a number: "))
    nums.append(number)

nums = sorted(nums)
nums.reverse()
print(nums)

#Challenge 89
nums = array('i',[])

for i in range(0,5):
    number = rand.randint(1,100)
    nums.append(number)

for i in nums:
    print(i)

#Challenge 90
nums = array('i',[])

for i in range(0,5):
    number = int(input("Please input a number between 10 and 20: "))

    while number < 10 or number > 20:
        print("Outside the range!")
        number = int(input("Try again! "))

    nums.append(number)

print("Thank you!")

for i in nums:
    print(i)

#Challenge 91
nums = array('i',[1,1,2,3,4])
print(nums)

number = int(input("Please enter a number: "))
count = nums.count(number)

print("Your chosen number appears",count,"times in the array")

#Challenge 92
user_array = array('i',[])
rand_array = array('i',[])

for i in range(0,3):
    number = int(input("Please input a number: "))
    user_array.append(number)

for j in range(0,5):
    number = rand.randint(1,100)
    rand_array.append(number)

user_array.extend(rand_array)
user_array = sorted(user_array)

for i in user_array:
    print(i)

Challenge 93
nums = array('i',[])

for i in range(0,5):
    number = int(input("Please input a number: "))
    nums.append(number)

nums = sorted(nums)
print("Your array is: ")

for i in nums:
    print(i)

to_remove = int(input("What number would you like to remove? "))

while to_remove not in nums:
    to_remove = int(input("The chosen number is not in the array! Try again!"))
    
nums.remove(to_remove)
print(nums)

#Challenge 94
nums = array('i',[])

for i in range(0,5):
    number = rand.randint(1,100)
    nums.append(number)

print("The array is: ")
for i in nums:
    print(i)

selection = int(input("Please select one of the numbers above: "))

while selection not in nums:
    selection = int(input("That is not a valid selection, please try again! "))

print("The position of your chosen number is", nums.index(selection) + 1)


#Challenge 95
nums = array('d',[95.33,10.88,18.99,20.79,35.84])
user_input = int(input("Please input a number between 2 and 5: "))
out_array = array('d',[])

while user_input < 2 or user_input > 5:
    user_input = int(input("I said between 2 and 5! Try again: "))

for i in nums:
    number = i / user_input
    out_array.append(number)

for j in out_array:
    print(round(j,2))
    
    






