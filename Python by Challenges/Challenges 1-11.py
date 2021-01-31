#Challenge 1
name = input("What is your name? ")
print("Hello ",name,"\n")

#Challenge 2
firstname = input("What is your first name?")
surname = input("what is your surname?")
print("Hello",firstname, surname,"\n")

#Challenge 3
print("What do you call a bear with no teeth?\nA gummy bear!\n")

#Challenge 4
num1 = int(input("Input your first number: "))
num2 = int(input("Input your second number: "))
Total = num1 + num2
print("The sum is",Total,"\n")

#Challenge 11
num1 = int(input("Enter a number larger than 100: "))

while num1 <= 100:
    print("I said larger than 100")
    num1 = int(input("Try again: "))

num2 = int(input("Enter a number smaller than 10: "))

while num2 >= 10:
    print("I said smaller than 10!")
    num2 = int(input("Try again: "))

result = num1 // num2
print("The second number divides into the larger number",result,"times")
