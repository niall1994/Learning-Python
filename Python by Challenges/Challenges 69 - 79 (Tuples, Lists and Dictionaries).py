###Challenge 69

country_tuple = ("Ireland","Germany","Spain","France","Denmark")
print(country_tuple)

user_input = input("Which country would you like to know the index for? ")
check = True

while check:
    for i in country_tuple:
        if user_input == i:
            check = False

    if check:
        user_input = input("Please input a value from the list provided above! ")

print("The index of the country you selected is:", country_tuple.index(user_input))

###Challenge 70 (Extension of 69)
user_index = int(input("Which index number would you like to return? "))
print("The country at your chosen index is", country_tuple[user_index])

###Challenge 71
sport_list = ["Football", "Rowing"]
user_sport = input("What is your favourite sport? ")
sport_list.append(user_sport)

print(sorted(sport_list))

###Challenge 72
subject_list = ["Maths","English","Physics","Design Communication Graphics", "Accounting", "Irish"]
print(subject_list)
unliked_subject = input("What subject from the above list do you not like? ")

check = True

while check:
    for i in subject_list:
        if unliked_subject == i:
            check = False

    if check:
        unliked_subject = input("Please input a value from the list provided above! ")

subject_list.remove(unliked_subject)
print(subject_list)

###Challenge 73
food_dictionary = {}
for i in range(1,5):
    fav_food = input("What is one of your favourite foods? ")
    food_dictionary[i] = fav_food

print(food_dictionary)
to_remove = int(input("Which index would you like to remove?"))
del food_dictionary[to_remove]
print(sorted(food_dictionary.values()))

#Challenge 79
nums = []
count = 0
while count < 3:
    new_num = input("Please input a number: ")
    nums.append(new_num)
    count = count + 1

    if count == 3:
        delete_last = input("Woudl you like to remove the last number? (Y/N) ")

        while delete_last != "N" and delete_last != "Y":
            delete_last = input("Only Y or N are valid inputs! ")

        if delete_last == "Y":
            nums.remove(new_num)

print(nums)
    
        

        
