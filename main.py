from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

word_dict = None


def random_word():
    global word_dict, flip_timer
    window.after_cancel(flip_timer)
    word_dict = random.choice(word_list)
    french_word = word_dict["French"]
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(word, text=f"{french_word}", fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global word_dict
    english_word = word_dict["English"]
    canvas.itemconfig(word, text=f"{english_word}", fill="white")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


def empty_func():
    pass


def true_answer():
    global word_dict, flip_timer
    window.after_cancel(flip_timer)
    word_dict = random.choice(word_list)
    french_word = word_dict["French"]
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(word, text=f"{french_word}", fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    flip_timer = window.after(3000, flip_card)
    word_list.remove(word_dict)
    dataframe = pd.DataFrame(word_list)
    dataframe.to_csv("words_to_learn.csv", index=False)


flip_timer = window.after(0, empty_func)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 273, image=card_front)
title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=true_answer)
right_button.grid(column=2, row=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=random_word)
wrong_button.grid(column=1, row=2)

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
finally:
    word_list = data.to_dict(orient="records")


window.mainloop()
