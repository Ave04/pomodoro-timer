import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timecounter = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timecounter)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text='Timer')
    checkmark.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        countdown(work_sec)
        timer.config(text="WORK", fg=GREEN)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="BREAK", fg=PINK)
    elif reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="BREAK", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif 0 < count_sec < 10:
        count_sec = '0' + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timecounter
        timecounter = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark =''
        for i in range(math.floor(reps/2)):
            mark += '✔'
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# tomato
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

# text displays
timer = tk.Label(text='Timer', font=(FONT_NAME, 40, 'bold'))
timer.config(fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

checkmark = tk.Label(text='', font=(FONT_NAME, 20, 'bold'))
checkmark.config(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

# start and reset buttons
start = tk.Button(text='Start', command=start_timer)
start.grid(column=0, row=2)

resetb = tk.Button(text='Reset', command=reset_timer)
resetb.grid(column=2, row=2)

window.mainloop()
