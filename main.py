import tkinter as tk



class QuizGameApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.root.geometry("700x400")

        self.welcome_label = tk.Label(root, text="Üdvözöllek a Quiz Játékomban!", font=("Arial", 16), pady=40)
        self.welcome_label.pack()

        self.start_button = tk.Button(root, text="Kezdés", font=("Arial", 14), command=self.start_quiz)
        self.start_button.pack(pady=40)

    def start_quiz(self):
        ...
        



if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()
