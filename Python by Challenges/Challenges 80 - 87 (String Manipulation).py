#Challenge 80
first_name = input("Please input your first name: ")
print("The length of your first name is", len(first_name), "\n")

sur_name = input("Please input your sur name: ")
print("The length of your sur name is: ", len(sur_name), "\n")

full_name = first_name + " " + sur_name
print("Your full name is",full_name, "Which has a length of", len(full_name),"\n")

#Challenge 81
fav_subject = input("What is your favourite school subject? ")

for letter in fav_subject:
    print(letter, end = "-")

print("\n")

#challenge 82
poem = "If you can bear to hear the truth youve spoken, twisted by knaves to make a trump for fools"
print(poem)

start = int(input("Which starting point would you like? "))
end = int(input("Which end point would you like? "))

print(poem[start-1:end])

#challenge 83

user_string = input("Please input a string all in upper case: ")

while user_string.isupper() == False:
    user_string = input("Try again! ")

print("Congratulations!")

#Challenge 84

post_code = input("What is your postcode? ")

for i in range(0,len(post_code)):
    if i == 0 or i == 1:
        print(post_code[i].upper(),end = "")
    else: 
        print(post_code[i].lower(),end ="")

print("\n")

###Challenge 85
user_name = input("What is your name? ")
vowels = ["A","E","I","O","U"]

user_name = user_name.upper()

vowel_count = 0

for letter in user_name:
    if letter in vowels:
        vowel_count = vowel_count + 1

print("Your name contains",vowel_count,"vowels","\n")

# Challenge 86
password = input("Please input a password: ")
verify_pass = input("Please verify your password: ")

if password == verify_pass:
    print("Password verified")
else:
    password = password.lower()
    verify_pass = verify_pass.lower()

    if(password == verify_pass):
        print("They must be the same case!")
    else:
        print("Incorrect")

# Challenge 87
user_string = input("Please input a string: ")
user_string_len = len(user_string)

for i in range(0,user_string_len):
    use_index = user_string_len - i
    print(user_string[use_index-1])

    

    

    


