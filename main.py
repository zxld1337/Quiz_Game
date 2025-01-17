import tkinter as tk
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
        

        self.root = root
        self.root.title("Quiz Game")

        self.root.geometry("700x400")

        self.welcome_label = tk.Label(root, text="Üdvözöllek a Quiz Játékomban!", font=("Arial", 16), pady=40)
        self.welcome_label.pack()

        self.start_button = tk.Button(root, text="Kezdés", font=("Arial", 14), command=self.start_quiz)
        self.start_button.pack(pady=40)


    def start_quiz(self):
        print(self.questions)
        



if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()
