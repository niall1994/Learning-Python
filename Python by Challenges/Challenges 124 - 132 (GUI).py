# Required Libraries
from tkinter import *
import random as rand
import csv

# Example
def Call():
    msg = Label(window,text = "You pressed the button!")
    msg.place(x = 30, y = 50)
    button["bg"] = "blue"
    button["fg"] = "white"

window = Tk()
window.geometry("200x110")
button = Button(text = "Press Me", command = Call)
button.place(x = 30, y = 20, width = 120, height = 25)
window.mainloop()

#Challenge 124
def click():
    name = entry_box.get()
    msg =  str("Hello " + name)
    output_box["bg"] = "yellow"
    output_box["fg"] = "blue"
    output_box["text"] = msg

window = Tk()
window.geometry("800x800")
window.title("Ask for the users name")

label = Label(text = "Enter your name: ")
label.place(x = 30, y = 10)
entry_box = Entry (text = "")
entry_box.place(x = 30, y = 50, width = 70)

button = Button(text = "Press Me", command = click)
button.place(x = 30, y = 90, width = 100)

output_box = Message(text = "")
output_box.place(x = 30, y = 110, width = 100)
output_box["bg"] = "black"
output_box["fg"] = "white"


# Challenge 125
def six_sided_die():
    result = rand.randint(1,6)
    output_box["text"] = str(result)

window = Tk()
window.geometry("400x800")
window.title("Roll a dice")

button = Button(text = "Press me to roll a dice!", command = six_sided_die)
button.place(x = 30, y = 50, width = 200)

output_box = Message(text = "Your result will be outputted here!")
output_box.place(x = 30, y = 70, height = 50)
output_box["bg"] = "black"
output_box["fg"] = "white"

#Challenge 126

def sum_cont():
    initial = int(output_box["text"])
    add = int(entry_box.get())
    msg = str(initial + add)
    output_box["text"] = msg

def reset():
    output_box["text"] = 0

window = Tk()
window.geometry("400x800")
window.title("Sum up a number")

label = Label(text = "Please enter a number below!")
label.place(x = 30, y = 20)

entry_box = Entry (text = 0)
entry_box.place(x = 30, y = 90, width = 50)

button_sum = Button(text = "sum", command = sum_cont)
button_sum.place(x = 30, y = 120, width = 100)

button_reset = Button(text = "Reset Counter", command = reset)
button_reset.place(x = 140, y = 120, width = 100)

output_box = Message(text = 0)
output_box.place(x = 30, y = 160)
output_box["bg"] = "red"

# Challenge 127
def add_name():
    input_name = entry_box.get()
    existing = output_box["text"]
    msg = existing + input_name + "\n"
    output_box["text"] = msg

def reset():
    output_box["text"] = ""

window = Tk()
window.title("Create a list of names")
window.geometry("400x800")

entry_box = Entry (text = "John Doe")
entry_box.place(x = 30, y = 20, width = 200)
entry_box["relief"] = "groove"

button_add_name = Button(text = "Add a name to the list", command = add_name)
button_add_name.place(x = 30, y = 50)

button_reset = Button(text = "Reset list", command = reset)
button_reset.place(x = 200, y = 50)

output_box = Message(text = "")
output_box.place(x = 30, y = 100, width = 200)
output_box["relief"] = "sunken"

# Challenge 128
def mile_to_kilometer():
    mile = float(entry_box_miles.get())
    result = mile * 1.6093
    output_box["text"] = result

def kilometer_to_mile():
    kilometer = float(entry_box_kilometer.get())
    result = kilometer * 0.6214
    output_box["text"] = result
    
window = Tk()
window.title("Kilometer/Mile converter")
window.geometry("400x800")

label_kilometer = Label(text = "Kilometer input")
label_kilometer.place(x = 30, y = 0)

entry_box_kilometer = Entry (text = "Kilometer")
entry_box_kilometer.place(x = 30, y = 20, width = 100)
entry_box_kilometer["relief"] = "groove"

button_kilometer = Button(text = "kilometer to miles", command = kilometer_to_mile)
button_kilometer.place(x = 30, y = 50, width = 150)

label_miles = Label(text = "Mile Input")
label_miles.place(x = 230, y = 0)

entry_box_miles = Entry (text = "Miles")
entry_box_miles.place(x = 230, y = 20, width = 100)
entry_box_miles["relief"] = "groove"

button_miles = Button(text = "miles to kilometers", command = mile_to_kilometer)
button_miles.place(x = 230, y = 50, width = 150)

output_box = Message(text = "")
output_box.place(x = 30, y = 200, width = 400)
output_box["relief"] = "sunken"

window.mainloop()

# Challenge 129
def add_to_list_box():
    input_var = entry_box.get()

    if input_var.isdigit() == True:
        list_box.insert(END, input_var)
        list_box.focus()
    else:
        entry_box.delete(0,END)

def clear_list():
    list_box.delete(0,END)
    list_box.focus()
    
window = Tk()
window.geometry("400x800")
window.title("Add to a list box")

entry_box = Entry (text = 0)
entry_box["relief"] = "groove"
entry_box.place(x = 30, y = 40)

button_add_list = Button(text = "Add to list", command = add_to_list_box)
button_add_list.place(x = 30, y = 100)

button_clear_list = Button(text = "Clear List", command = clear_list)
button_clear_list.place(x = 130, y = 100)

list_box = Listbox()
list_box.place(x = 30, y = 150)

# Challenge 130
def add_to_list_box():
    input_var = entry_box.get()

    if input_var.isdigit() == True:
        list_box.insert(END, input_var)
        list_box.focus()
    else:
        entry_box.delete(0,END)

def clear_list():
    list_box.delete(0,END)
    list_box.focus()

def save_list():
    tmp_list = list_box.get(0,END)

    file = open("List.csv","w")

    for i in range(0,len(tmp_list)):
        new_record = tmp_list[i] + ","
        file.write(new_record)

    file.close()
    

window = Tk()
window.geometry("400x800")
window.title("Add to a list box")

entry_box = Entry (text = 0)
entry_box["relief"] = "groove"
entry_box.place(x = 30, y = 40)

button_add_list = Button(text = "Add to list", command = add_to_list_box)
button_add_list.place(x = 30, y = 100)

button_clear_list = Button(text = "Clear List", command = clear_list)
button_clear_list.place(x = 130, y = 100)

button_save_list = Button(text = "Save List to CSV", command = save_list)
button_save_list.place(x = 30, y = 125)

list_box = Listbox()
list_box.place(x = 30, y = 150)

# Challenge 131
def save_to_csv():
    file = open("Names and Ages.csv","a")
    name = entry_box_name.get()
    age = entry_box_age.get()
    NewRecord = name + "," + age + "\n"
    file.write(NewRecord)
    file.close()
    button_save_csv["bg"] = "blue"
    
window = Tk()
window.title("Create list of names")
window.geometry("400x800")

label_name = Label(text = "Enter the persons name below!")
label_name.place(x = 0, y = 0)

entry_box_name = Entry (text = "Name")
entry_box_name.place(x = 0, y = 50)

label_age = Label(text = "Enter the persons age below!")
label_age.place(x = 200, y = 0)

entry_box_age = Entry (text = "Age")
entry_box_age.place(x = 200, y = 50)

button_save_csv = Button(text = "Append name to CSV file", command = save_to_csv)
button_save_csv.place(x = 0, y = 100)

# Challenge 132
def save_to_csv():
    file = open("Names and Ages.csv","a")
    name = entry_box_name.get()
    age = entry_box_age.get()
    NewRecord = name + "," + age + "\n"
    file.write(NewRecord)
    file.close()
    button_save_csv["bg"] = "blue"

def import_to_list():
    names = list(csv.reader(open("Names and Ages.csv")))
    tmp = []

    for i in names:
        tmp.append(names)

    name_list.delete(0,END)

    x = 0
    for i in names:
        data = tmp[x]
        name_list.insert(END,data)
        x = x + 1

    name_list.focus()
    
window = Tk()
window.title("Create list of names")
window.geometry("400x800")

label_name = Label(text = "Enter the persons name below!")
label_name.place(x = 0, y = 0)

entry_box_name = Entry (text = "Name")
entry_box_name.place(x = 0, y = 50)

label_age = Label(text = "Enter the persons age below!")
label_age.place(x = 200, y = 0)

entry_box_age = Entry (text = "Age")
entry_box_age.place(x = 200, y = 50)

button_save_csv = Button(text = "Append name to CSV file", command = save_to_csv)
button_save_csv.place(x = 0, y = 100)

button_import_to_list = Button(text = "Import to List", command = import_to_list)
button_import_to_list.place(x = 200, y = 100)

name_list = Listbox()
name_list.place(x = 0, y = 150)
