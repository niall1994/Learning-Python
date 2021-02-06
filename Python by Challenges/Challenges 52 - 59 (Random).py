import random as rand

#challenge 52
rand_int = rand.randint(1,100)
print(rand_int,"\n")

#challenge 53
fruit_list = ("apple", "orange", "pear", "banana", "strawberry")
rand_fruit = rand.choice(fruit_list)
print(rand_fruit,"\n")

#challenge 54
outcome_list = ("H","T")
user_guess = input("Heads or Tails? (H/T)")
check = False

if user_guess != "H":
    if user_guess != "T":
        check = True

while check:
    print("Only inputs H and T are valid, please pick again!")
    user_guess = input("Heads or Tails? (H/T)")

    if user_guess == "H":
        check = False
    elif user_guess == "T":
        check = False

compute_guess = rand.choice(outcome_list)

if user_guess == compute_guess:
    print("Congratulations!, you guessed correct!")
else:
    print("Bad Luck")

print("The computer flipped a", compute_guess, "\n")

#Challenge 59
colors = ("green", "blue", "red", "orange", "white")
compute = rand.choice(colors)

print("Please pick from one of the following colors:")
for col in colors:
    print(col)

user_guess = input("What color do you think the computer will choose? ").lower()
test = True

while test:
    if user_guess == compute:
        test = False
        print("Congratulations, you chose correctly!")
    elif compute == "green":
        print("Ohhh, you must be GREEN with envy for missing that one!")
        user_guess = input("Lets guess again! ").lower()
    elif compute == "blue":
        print("Dont feel too BLUE about missing that one!")
        user_guess = input("Lets guess again! ").lower()
    elif compute == "red":
        print("I guess your RED with anger!")
        user_guess = input("Lets guess again! ").lower()
    elif compute == "orange":
        print("Maybe you should take a break and have an ORANGE!")
        user_guess = input("Lets guess again! ").lower()
    elif compute == "white":
        print("I guess youve been looking at WHITE screens for too long!")
        user_guess = input("Lets guess again! ").lower()
