BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial",40, "italic")
BODY_FONT = ("Arial",60, "bold")

from tkinter import *
from tkinter import messagebox
import random
import json
import pandas as pd

current_card =[]

def action():
    pass


def change_side():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(body_text, text= current_card[1], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")

def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    current_card = random.choice(data_list)
    canvas.itemconfig(body_text, text= current_card[0], fill="black")
    canvas.itemconfig(title_text, text="Frech", fill="black")
    flip_timer = window.after(3000, change_side)
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 258, image=card_front)
title_text = canvas.create_text(400,150, text = "Frech", fill= "black", font = TITLE_FONT)
body_text = canvas.create_text(400,263, text = "trouve", fill= "black", font = BODY_FONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
right = Button(image=right_img, highlightthickness=0, command=change_word)
right.grid(column=1, row=1)

flip_timer = window.after(2000, change_side)

data = pd.read_csv("./data/french_words.csv")
data_list = data.values.tolist()

change_word()



#




window.mainloop()
