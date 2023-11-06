from tkinter import *
THEME_COLOR = "#375362"
FONT = ("Arial",20,"italic")

class QuizInterface:

    def __init__(self):
        self.window= Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.score_label = Label(text="score : 0",bg=THEME_COLOR, font=("Arial",12,"normal"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300,)
        self.qc_text = self.canvas.create_text(150,125,text="j", font=FONT)
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)
        
        self.check_image = PhotoImage(file="API/quizer/images/true.png")
        self.true_button = Button(image=self.check_image)
        self.true_button.grid(row=2,column=0)


        self.cross_image = PhotoImage(file="API/quizer/images/false.png")
        self.false_button = Button(image=self.cross_image, )
        self.false_button.grid(row=2, column=1)




    def change_text(self, qu):
        print(qu)
        self.canvas.itemconfig(self.qc_text, text=qu)
        

