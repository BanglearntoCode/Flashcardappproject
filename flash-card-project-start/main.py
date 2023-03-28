from tkinter import *
from random import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.config(pady=0, padx=0, bg=BACKGROUND_COLOR)
window.title("Flash Card App")

#function to find new words
try:
    data = pandas.read_csv("./data/words_to_learn")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
random_word = {}


def find_a_new_word():
    global random_word, timer
    window.after_cancel(timer)
    random_word = choice(data_dict)
    canvas1.itemconfig(english, text="France", fill="black")
    canvas1.itemconfig(france, text=random_word["French"], fill="black")
    canvas1.itemconfig(front, image=front_ground)
    timer = window.after(3000, find_meaning)


def find_meaning():
    meaning = random_word["English"]
    canvas1.itemconfig(front, image=background)
    canvas1.itemconfig(english, text="English", fill="white")
    canvas1.itemconfig(france, text=meaning, fill="white")


timer = window.after(3000, find_meaning)


def is_known():
    data_dict.remove(random_word)
    word_to_learn = pandas.DataFrame(data_dict)
    word_to_learn.to_csv("data/words_to_learn", index=False)
    find_a_new_word()

#create canvas

canvas1 = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_ground = PhotoImage(file="./images/card_front.png")
background = PhotoImage(file="./images/card_back.png")
front = canvas1.create_image(400, 263, image=front_ground)
english = canvas1.create_text(400, 150, text="", fill="black", font=("Arial", 40))
france = canvas1.create_text(400, 320, text="", fill="black", font=("Arial", 60, "bold"))
canvas1.grid(row=0, column=0, pady=50, padx=50, columnspan=2)

#create buttons
x_button = Button(text="❌", font=("Arial", 32), fg="red", command=find_a_new_word)
x_button.grid(row=1, column=0, pady=50)
v_button = Button(text="✅", font=("Arial", 32), fg="green", command=is_known)
v_button.grid(row=1, column=1, pady=50)

find_a_new_word()
window.mainloop()


