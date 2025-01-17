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
        self.player_answers = []
        
        self.root = root
        self.root.title("Quiz Game")

        self.root.geometry("700x400")

        self.welcome_label = tk.Label(root, text="Üdvözöllek a Quiz Játékomban!", font=("Arial", 16), pady=40)
        self.welcome_label.pack()

        self.start_button = tk.Button(root, text="Kezdés", font=("Arial", 14), command=self.play_quiz)
        self.start_button.pack(pady=40)


    def play_quiz(self):
        if (self.used) >= len(self.questions):
            self.show_result_screen()
                    
        for widget in self.root.winfo_children():
            widget.destroy()

        quiz = self.get_new_question()
        self.used.append(quiz)
            
        self.question_label = tk.Label(self.root, text=quiz.question, font=("Arial", 16), pady=20)
        self.question_label.pack()

        random.shuffle(quiz.answers)

        for answer in quiz.answers:
            button = tk.Button(
                self.root,
                text=answer,
                font=("Arial", 14),
                command=lambda ans=answer: self.answer_selected(ans, quiz["correct"])
            )
            button.pack(pady=10)
        

        


    def save_selected(self, answer):
        self.player_answers.append(answer)


    def get_new_question(self):
        temp = None
        not_used = True 
        while not_used:
            temp = random.choice(self.questions)
            if temp not in self.used:
                not_used = False
        
        return temp
    

    
        

        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()
