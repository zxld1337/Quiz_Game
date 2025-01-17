import tkinter as tk
import random
from dataclasses import dataclass


QUESTIONS = [
    ["Melyik nem József Attila műve?", "Vér és arany", "Nem én kiáltok", "külvárosi éj"],
    ["Melyik bolygó a Naprendszer legnagyobbja?", "Jupiter", "Mars", "Föld"],
    ["Mi a HTML jelentése?", "HyperText Markup Language", "Home Tool Markup Language", "Hyper Transfer Markup Language"],
    ["Ki írta a Hamlet-et?", "William Shakespeare", "Charles Dickens", "Leo Tolstoy"],
    ["Melyik elemnek a vegyjele H?", "Hidrogén", "Hélium", "Halogén"],
    ["Melyik évben tört ki az első világháború?", "1914", "1939", "1918"],
    ["Melyik adatstruktúra használja a LIFO (Last In, First Out) elvet?", "Stack", "Queue", "Tree"],
    ["Melyik ország fővárosa Párizs?", "Franciaország", "Olaszország", "Spanyolország"],
    ["Melyik eseményt tartják a reformáció kezdetének?", "Luther 95 tételének kifüggesztése", "A francia forradalom", "Az amerikai függetlenségi háború"],
    ["Melyik folyamat során alakul ki a szén-dioxid?", "Égés", "Fotoszintézis", "Párolgás"]
]


@dataclass
class Question:
    question: str
    answers: list[str]
    correct: str

    @classmethod
    def form(cls, item):
        return cls(item[0], item[1:], item[1])
    
    @staticmethod
    def fromList(list):
        return [Question.form(x) for x in list]



class QuizGameApp:
    def __init__(self, root):
        self.questions = Question.fromList(QUESTIONS) 
        self.used = []
        self.player_corrects = 0
        
        self.root = root
        self.root.title("Quiz Game")

        self.root.geometry("700x400")
        self.welcome_screen()


    def welcome_screen(self):
        welcome_label = tk.Label(root, text="Üdvözöllek a Quiz Játékomban!", font=("Arial", 16), pady=40)
        welcome_label.pack()

        start_button = tk.Button(root, text="Kezdés", font=("Arial", 14), command=self.play_quiz)
        start_button.pack(pady=40)


    def play_quiz(self):                            
        for widget in self.root.winfo_children():
            widget.destroy()

        quiz = self.get_new_question()
        self.used.append(quiz)
            
        self.question_label = tk.Label(self.root, text=quiz.question, font=("Arial", 16), pady=40)
        self.question_label.pack()

        random.shuffle(quiz.answers)

        for answer in quiz.answers:
            button = tk.Button(
                self.root,
                text=answer,
                font=("Arial", 14),
                command=lambda ans=answer: self.answer_selected(answer, quiz.correct)
            )
            button.pack(pady=10)    
        


    def answer_selected(self, answer, correct):
        if answer == correct:
            self.player_corrects += 1

        if len(self.used) < len(self.questions):
            self.root.after(200, self.play_quiz)
        else:
            self.root.after(200, self.show_result_screen)


    def get_new_question(self):
        temp = None
        not_used = True 
        while not_used:
            temp = random.choice(self.questions)
            if temp not in self.used:
                not_used = False
        
        return temp
    

    def show_result_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        results_label = tk.Label(self.root, text="Gratulálok!", font=("Arial", 16), pady=20)
        results_label.pack()

        results_label = tk.Label(self.root, text="A quiz véget ért", font=("Arial", 16), pady=20)
        results_label.pack()

        score_label = tk.Label(self.root, text=f"A jó válaszaid száma: {len(self.used)}/{self.player_corrects}", font=("Arial", 14), pady=20)
        score_label.pack()

        new_game_button = tk.Button(self.root, text="Újra probálom", font=("Arial", 14), command=self.reset_game)
        new_game_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Kilépés", font=("Arial", 14), command=self.root.quit)
        exit_button.pack(pady=10)


    def reset_game(self):
        self.used = []
        self.player_corrects = 0

        for widget in self.root.winfo_children():
            widget.destroy()

        self.welcome_screen()

        

            

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()
