import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#87CEEB"

class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzer")
        self.window.minsize(width=350, height=560)
        self.window.configure(background=THEME_COLOR)
        self.window.config(padx=30, pady=22)

        self.score = 0
        self.score_label = tk.Label(text=f"Score {self.score}", background=THEME_COLOR, font=("Calibri", 17, "bold"))
        self.score_label.grid(row=0, column=2)

        self.canvas = tk.Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question Goes Here",
                                                     width=280,
                                                     font=("Arial", 16, "italic")
                                                     )
        self.canvas.grid(row=1, column=1, columnspan=2, pady=20)

        correct_image = tk.PhotoImage(file=r"images//true.png")
        self.correct_button = tk.Button(image=correct_image, highlightthickness=0, command=self.user_says_true)
        self.correct_button.grid(row=2, column=1)

        wrong_image = tk.PhotoImage(file=r"images//false.png")
        self.wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=self.user_says_false)
        self.wrong_button.grid(row=2, column=2)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        ques_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=ques_text)

    def user_says_true(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def user_says_false(self):
        self.quiz.check_answer("False")
        self.get_next_question()



