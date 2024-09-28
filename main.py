import math
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE

timer_text = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    start_button["state"] = ACTIVE
    start_button["fg"] = RED
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 35, "bold" ))



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button['state'] = DISABLED

    global reps
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="LONG BREAK", fg=RED)
        countdown(20 * 60)

    if reps % 2 == 1:
        title_label.config(text="WORK", fg=GREEN)
        countdown(10)
    elif reps % 2 == 0:
        title_label.config(text="SHORT BREAK", fg=PINK)
        countdown(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    minute = math.floor(count / 60)
    second = count % 60
    if minute < 10:
        minute = f"0{minute}"
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    global timer
    if count > 0:
        timer = window.after(1000, countdown, count - 1)

    if count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# making the window
window = Tk()
# window.minsize(width=4, height=400 )
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 30), fg="green", bg=YELLOW)
title_label.grid(column=1, row=0)

# canvas declaration
# highlightthickness is used to remove the thickness of the border of the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=RED, width=10, height=1, fg="white", command=start_timer)
reset_button = Button(text="Reset", bg=RED, width=10, heigh=1, fg="white", command=reset)
start_button.grid(column=0, row=3)
reset_button.grid(column=3, row=3)

checkmark = Label(text="✔", fg="green", bg=YELLOW)
# checkmark.grid(column=1, row=3)


window.mainloop()
