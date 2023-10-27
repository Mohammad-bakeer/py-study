from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BT_FONT = (FONT_NAME, 12, "bold")
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    check_mark_label.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(text_timer, text="00:00")
    reps=0
    
# ---------------------------- TIMER MECHANISM ------------------------------- #
def strat_timer():
    global reps 
    reps +=1
    work_sec = 60 * WORK_MIN
    short_break = 60 * SHORT_BREAK_MIN
    long_break = 60 * LONG_BREAK_MIN

    if reps %8 == 0:
        timer_label.config(text="break", fg=RED)
        count_down(3)
    elif reps %2 == 0:
        timer_label.config(text="break", fg=PINK)
        count_down(2)
    else:
        timer_label.config(text="work", fg=GREEN)
        count_down(2)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(text_timer, text="%02d:%02d" % (count_min, count_sec))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        strat_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
ph = PhotoImage(file="tkinter/tkinter_2/tomato.png")
canvas.create_image(100, 112, image=ph)
text_timer = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(
    FONT_NAME, 48, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=BT_FONT,
                      highlightthickness=0, command=strat_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=BT_FONT,
                      highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark_label = Label( font=(
    FONT_NAME, 15, "normal"), bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=1, row=3)

window.mainloop()
