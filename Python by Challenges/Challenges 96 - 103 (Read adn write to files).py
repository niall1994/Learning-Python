 Required Libraries
import csv
import random as rand
#Challenge 105
file = open("Numbers.txt","w")
file.write("1,")
file.write("2,")
file.write("3,")
file.write("4,")
file.close()

###Challenge 106
file = open("Names.txt","w")
file.write("Tom\n")
file.write("James\n")
file.write("Eoghan\n")
file.write("Aaron\n")
file.write("Tim\n")
file.close()

#challenge 107
file = open("Names.txt","r")
print(file.read())

#Challenge 108
file = open("Names.txt","a")
new_name = input("What name would you like to add to the file? ")
file.write(new_name)
file.close()

file = open("Names.txt","r")
print(file.read())

#Challenge 109
from array import *
print("1) Crate a new file\n2) Display the file\n3)Add a new item to the file")

choices = array('i',[1,2,3])
selection = int(input("What would you like to do?"))

while selection not in choices:
    selection = int(input("Only entries 1,2 or 3 are valid. Please try again! "))

if selection == 1:
    subject = input("Please enter a school subject: ")
    file = open("Subject.txt","w")
    file.write(subject + "\n")
    file.close()
elif selection == 2:
    file = open("Subject.txt","r")
    print(file.read())
    file.close()
elif selection == 3:
    file = open("Subject.txt","a")
    new_subject = input("What subject would you like to add? ")
    file.write(new_subject + "\n")
    file.close()
    file = open("Subject.txt","r")
    print(file.read())
    file.close()


#Challenge 110
file = open("Names.txt","r")
to_remove = input("What name would you like to remove?") + "\n"

for rows in file:
    if rows != to_remove:
        file2 = open("Names2.txt","a")
        file2.write(rows)

file2.close()
file.close()

#Challenge 111
import csv

file = open("Books.csv","w")
record = "Book, Author, Year\n"
file.write(record)
record = "To Kill a Mocking Board, Harper Lee, 1960\n"
file.write(record)
record = "A brief history of time, Stephen Hawking, 1988\n"
file.write(record)
record = "The great gatsby, F.Scot Fitzgerald, 1922\n"
file.write(record)
record = "The man who mistook his wife for a hat, Oliver Sacks, 1985\n"
file.write(record)
record = "Pride and Predjudice, Jane Austin, 1813\n"
file.write(record)
file.close()

#Challenge 112
file = open("Books.csv","r")
print(file.read())
file.close()

file = open("Books.csv","a")
title = input("What title would you like to add? ") + ","
author = input("What author would you like to add? ") + ","
year = input("What year was the title written? ") + "\n"

newrecord = title + author + year
file.write(newrecord)
file.close()

file = open("Books.csv","r")
for row in file:
    print(row)

file.close()

# Challenege 11
file = open("Books.csv","a")

number_of_entries = int(input("How many entries would you like to make? "))
count = 0

while count < number_of_entries:
    title = input("What title would you like to add? ") + ","
    author = input("What author would you like to add? ") + ","
    year = input("What year was the title written? ") + "\n"
    newrecord = title + author + year
    file.write(newrecord)
    count = count + 1
    
file.close()


select_author = input("What author would you like to view? ")
file = open("Books.csv","r")
for row in file:
    if select_author in row: 
        print(row)

file.close()

# Challenge 114
file = list(csv.reader(open("Books.csv")))

start_year = int(input("What starting year would you like?"))
end_year = int(input("What end year would you like"))

for row in file:
  if row[2] != " Year":      
    year = int(row[2])
    
    if year >= start_year:
        if year <= end_year:
            print(row)

Challenge 115
file = list(csv.reader(open("Books.csv")))
count = 1

for row in file:
    print(row, count)
    count = count + 1

# Challenge 116
file = list(csv.reader(open("Books.csv")))
print(file)

row_to_remove = int(input("Which row would you like to remove? "))
del file[row_to_remove]
print(file)
row_to_change = int(input("Which row would you like to change? "))
print(file[row_to_change])
col_to_change = int(input("Which Column would you like to change? "))
new_data = input("What value would you like? ")
file[row_to_change][col_to_change] = new_data

file_new = open("Books.csv","w")
i = 0
for element in file:
    new_record = file[i][0] + ',' + file[i][1] + ',' + file[i][2] + "\n"
    file_new.write(new_record)
    i = i + 1
file_new.close()

# Challenge 117
name = input("What is your name? ")
options = ["M","D","A","S"]

nums = [rand.randint(1,100),rand.randint(100,200),rand.randint(1,100),rand.randint(100,200)]
equations = [rand.choice(options),rand.choice(options)]
answers = [0,0]
user_answers = [0,0]
questions = ["",""]
score = 0

for i in range(0,2):
    if equations[i] == "M":
        answers[i] = nums[i] * nums[i + 1]
        questions[i] = "What_is_" + str(nums[i])+ "_*_" + str(nums[i + 1])
        user_answers[i] = float(input(questions[i] + " "))

        if user_answers[i] == answers[i]:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect. You said",user_answers[i],"You should have said",answers[i])
            
    elif equations[i] == "D":
        answers[i] = round(nums[i] / nums[i + 1],2)
        questions[i] = "What_is_" + str(nums[i])+ "_/_" + str(nums[i + 1])
        user_answers[i] = float(input(questions[i] + " "))
        
        if user_answers[i] == answers[i]:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect. You said",user_answers[i],"You should have said",answers[i])
            
    elif equations[i] == "A":
        answers[i] = nums[i] + nums[i + 1]
        questions[i] = "What_is_" + str(nums[i])+ "_+_" + str(nums[i + 1])
        user_answers[i] = float(input(questions[i] + " "))
        
        if user_answers[i] == answers[i]:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect. You said",user_answers[i],"You should have said",answers[i])
            
    else:
        answers[i] = nums[i] - nums[i + 1]
        questions[i] = "What_is_" + str(nums[i])+ "_-_" + str(nums[i + 1])
        user_answers[i] = float(input(questions[i] + " "))
        
        if user_answers[i] == answers[i]:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect. You said",user_answers[i],"You should have said",answers[i])

print("Your Score is:",score)

file = open("Math Exam Results.csv","a")

newRecord = name + "," + questions[0] + "," + str(user_answers[0]) + "," + str(answers[0]) + "," + questions[1] + "," + str(user_answers[1]) + "," + str(answers[1]) + "," + str(score) + "\n"

file.write(newRecord)
file.close()


