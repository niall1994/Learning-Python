#Challenge 12
num1 = int(input("Please input a number "))
num2 = int(input("Please input another number "))

if num1 > num2:
    print(num2,num1,"\n")
else:
    print(num1, num2,"\n")

#Challenge 13
number = int(input("Please input a number smaller than 20 "))
if number >= 20:
    print("Too high!","\n")
else:
    print("Thank you!","\n")

#Challenge 19
num = int(input("Please input a 1,2 or 3 "))

if num == 1:
    print("Thank You!")
elif num == 2:
    print("Well Done")
elif num == 3:
    print("Correct")
else:
    print("Error message")
