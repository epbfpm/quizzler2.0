from tkinter import *
from quiz_brain import QuizBrain

import data

THEME_COLOR = "#375362"


class QuestionInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_lbl = Label(padx=40, text='Acertos: 0/10', fg='white', bg=THEME_COLOR, font=('Arial', 15))
        self.score_lbl.grid(column=1, row=0, columnspan=3)

        self.canvas = Canvas(height=300, width=300, bg='white')
        self.question_text = self.canvas.create_text(150, 150, text='self.get_next_question()',
                                                     font=('Arial', 18, 'italic'), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=1, row=1, columnspan=2, padx=40, rowspan=2)

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        self.true = Button(padx=40, image=true_img, bd=0, highlightthickness=0, command=self.right)
        self.true.grid(column=3, row=1)

        self.false = Button(padx=40, image=false_img, bd=0, highlightthickness=0, command=self.wrong)
        self.false.grid(column=3, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_next = self.quiz.next_question()
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.canvas.itemconfig(self.question_text, text=q_next)

    def right(self):
        self.result(self.quiz.check_answer('True'))

    def wrong(self):
        self.result(self.quiz.check_answer('False'))

    def result(self, result):
        if result:
            self.score_lbl.config(text=f'Acertos: {self.quiz.score}/10')
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.question_text, fill='white')
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.question_text, fill='white')
        if self.quiz.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg='white')
            self.true.config(state='disabled')
            self.false.config(state='disabled')
            self.canvas.itemconfig(self.question_text, text=f'Sua pontuação final é: {self.quiz.score}/10', fill=THEME_COLOR)

