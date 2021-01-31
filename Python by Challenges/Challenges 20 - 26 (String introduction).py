#Challenge 20
name = input("What is your name? ")
result = len(name)
print("Your name has", result, "letters\n")

#Challenge 21
first_name = input("What is your first name? ")
surname = input("What is your surname? ")
full_name = first_name + " " + surname
length = len(full_name) - 1
print("Your name is:", full_name)
print("It has a total of:",length,"letters\n")

#Challenge 22
first_name = input("What is your first name? (In lower case) ")
surname = input("What is your surname? (In lower case) ")
first_name = first_name.title()
surname = surname.title()
full_name = first_name + " " + surname
print(full_name)

#Challenge 23
rhyme = input("Please input the first line of nursery rhyme: ")
length = len(rhyme)
print("The length of the string is: ",length,"\n")
start = int(input("What staring point would you like? ")) - 1
end = int(input("What end point would you like? "))
print(rhyme[start:end])

#Challenege 24
str = input("Please input any string: ")
print(str.upper(),"\n")

#challenge 25
first_name = input("What is your first name: ")
length = len(first_name)

if length < 5:
    surname = input("Please enter your surname: ")
    full_name = first_name + surname
    print(full_name.upper(),"\n")
else:
    print(first_name.lower(),"\n")

#Challenge 26
orig_str = input("Please input any word, and I will convert it to Pig Latin! ")
orig_str = orig_str.lower()
first_letter = orig_str[0]

if first_letter == "a":
    print(orig_str + "way")
elif first_letter == "e":
    print(orig_str + "way")
elif first_letter == "i":
    print(orig_str + "way")
elif first_letter == "o":
    print(orig_str + "way")
elif first_letter == "u":
    print(orig_str + "way")
else:
    print(orig_str[1:] + first_letter + "ay")
