from tkinter import *
from tkinter import messagebox
import random
import json

import pyperclip as pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pw_generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice((letters)) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for sym in range(nr_symbols)]

    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password: str = "".join(password_list)
    pw_entry.delete(0, END)
    pw_entry.insert(END, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# # tke input in web/ user/password
# Add - save data into a file data.text
#
# new line
# append to the end of the entry
#
# # websoite | email | password


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, bd=0, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
# timer_text = canvas.create_text(110,130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)


# label1.config(padx = 5, pady=5, bg= YELLOW, fg = GREEN, font = (FONT_NAME,80,"bold"))

def writetofile():
    web = web_entry.get()
    email = email_entry.get()
    pw = pw_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": pw
        }
    }

    if web == "" or pw == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        #Reading old data file
        try:
            data_file = open("data.json", "r")
        except FileNotFoundError:
            data_file = open("data.json", "w")
            json.dump(new_data, data_file, indent=4)
            data_file.close()
        else:

            data = json.load(data_file)
            #Update old data with new data
            data.update(new_data)
            data_file.close()
            #Saving updated data
            data_file = open("data.json", "w")
            json.dump(data, data_file, indent = 4)
            data_file.close()

        finally:
            web_entry.delete(0, END)
            pw_entry.delete(0, END)

def search():
    try:
        data_file = open("data.json", "r")
        data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(message="Error: No data found")
    else:
        search = web_entry.get()
        if search in data:
            messagebox.showinfo(title=search, message= f"Email: {data[search]['email']} \n Password: {data[search]['password']}"
            )
        else:
            messagebox.showinfo(title=search, message=f"No data found")

web_entry = Entry(width=21)
web_entry.insert(END, string="")
web = web_entry.get()
web_entry.grid(column=1, row=1)
web_entry.focus()
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(END, string="vndnghi@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
email = email_entry.get()

pw_label = Label(text="Password: ")
pw_label.grid(column=0, row=3)

pw_entry = Entry(width=21)
pw_entry.insert(END, string="")
pw_entry.grid(column=1, row=3)
pw = pw_entry.get()

generate_button = Button(text="Generate Password", command=pw_generator)
generate_button.grid(column=2, row=3)

search_button = Button(width=13, text="Search", command=search)
search_button.grid(column=2, row=1)

add_button = Button(width=36, text="Add", command=writetofile)
add_button.grid(column=1, row=4, columnspan=2)
#
# button1 = Button(text="Start", command= start_timer, highlightthickness=0, fg =PINK)
# button1.grid(column =0, row =2)
#
# button2 = Button(text="Reset", command=reset_timer, highlightthickness=0,fg =PINK)
# button2.grid(column =2, row =2)
#
# tick = Label(text="")
# tick.grid(column = 1, row = 3)
# tick.config(padx = 5, pady=5, bg= YELLOW, fg = GREEN, font = (FONT_NAME,30,"bold"))
#
# # "✓"
#


window.mainloop()
