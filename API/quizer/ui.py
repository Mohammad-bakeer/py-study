from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizInterface:

    def __init__(self, quiz_b:QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.quiz = quiz_b

        self.score_label = Label(
            text="score : 0", bg=THEME_COLOR, font=("Arial", 12, "normal"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300,)
        self.qc_text = self.canvas.create_text(150, 125, text="j",width=280 ,font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.check_image = PhotoImage(file="API/quizer/images/true.png")
        self.true_button = Button(image=self.check_image, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        self.cross_image = PhotoImage(file="API/quizer/images/false.png")
        self.false_button = Button(
            image=self.cross_image, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()



    def get_next_question(self):
        qu = self.quiz.next_question()
        self.canvas.itemconfig(self.qc_text, text=qu)

    def is_true(self):
        x = self.quiz.check_answer("True")            
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.qc_text, text="You've completed the quiz")


    def is_false(self):
        x = self.quiz.check_answer("False")
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.qc_text, text="You've completed the quiz")

