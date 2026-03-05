import customtkinter as ctk

class KBCQuiz(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KBC Quiz Game")
        self.geometry("800x600")
        self.resizable (False, False)

        self.questions = [
            {
                "q": "Who is the President of U.S.A?",
                "o": ["Narendra Modi", "Joe Biden", "Donald Trump", "Vladimir Putin"],
                "a": 2
            },
            {
                "q": "Which Cricketer has the most centuries in One Day Internationals (O.D.I)?",
                "o": ["Sachin Tendulkar", "Ricky Ponting", "Thala", "Virat Kohli"],
                "a": 3
            },
            {
                "q": "Which is the highest grossing Indian movie worldwide?",
                "o": ["Dangal (2016)", "Bahubali 2 (2017)", "Dhurandar (2025)", "Pushpa 2 (2024)"],
                "a": 0
            },
            {
                "q": "Who is the Richest man in the world?",
                "o": ["Mark Zuckerberg", "Bill Gates", "Suneo (Doramon)", "Elon Musk"],
                "a": 3
            },
            {
                "q": "Which one of the following is the highest rated web show on imdb",
                "o": ["Stranger Things", "Breaking Bad ", "Game of Thrones", "Dark"],
                "a": 1
            },
            {
                "q": "The 'Kathak' dance form is originated from which state ?",
                "o": ["Tamil Nadu", "Karnataka", "Uttar Pradesh", "Rajasthan"],
                "a": 2
            },
            {
                "q": "Which country has won the most FIFA world cup titles ?",
                "o": ["Argentina", "Germany", "Portugal", "Brazil"],
                "a": 3
            },
            {
                "q": "How many Vedas are there in Hinduism?",
                "o": ["Three", "Eighteen", "Four", "fourteen"],
                "a": 2
            },
            {
                "q": "Who created Python  ?",
                "o": ["Dennis Ritchie", "Dekisugi (Doraemon)", "Tim Berners Lee", "Guido Van Rossum"],
                "a": 3
            },
            {
                "q": "Which major character of MCU died in the 'Battle of Earth' in Avengers Endgame ?",
                "o": ["Tony Stark", "Steve Rogers", "Clint Barten", "Peter Quill"],
                "a": 0
            },

        ]
        self.current = 0
        self.score = 0 


        #------------------------User Interface-----------------------
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.score_label = ctk.CTkLabel(
            self.main_frame,
            text="Score: 0",
            font=("Arial", 16)
        )
        self.score_label.pack(anchor="ne")

        self.question_label = ctk.CTkLabel( 
            self.main_frame,
            text="",
            wraplength=520,
            font=("Arial", 18)
        )
        self.question_label.pack(pady=20)

        self.buttons_frame = ctk.CTkFrame(self.main_frame)
        self.buttons_frame.pack(pady=10)

        self.option_buttons = []

        for i in range(4):
            btn = ctk.CTkButton(
                self.buttons_frame,
                text="",
                width=250,
                command=lambda i=i: self.check_answer(i)
            )
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            self.option_buttons.append(btn)

        self.result_label = ctk.CTkLabel(
            self.main_frame,
            text="",
            font=("Arial", 16)
        )
        self.result_label.pack(pady=10)

        self.load_question()

    def load_question(self):

        if self.current >= len(self.questions):
            self.show_final_screen()
            return

        quedata = self.questions[self.current]

        self.question_label.configure(
            text=f"Q{self.current + 1}. {quedata['q']}"
        )

        for i in range(4):
            self.option_buttons[i].configure(
                text=f"{chr(65+i)}. {quedata['o'][i]}",
                state="normal"
            )

        self.result_label.configure(text="")

    def check_answer(self, index):

        for btn in self.option_buttons:
            btn.configure(state="disabled")

        correct_index = self.questions[self.current]["a"]

        if index == correct_index:
            self.score += 1
            self.result_label.configure(text="Correct!")
        else:
            correct_text = self.questions[self.current]["o"][correct_index]
            self.result_label.configure(
                text=f"Wrong! Correct answer: {correct_text}"
            )

        self.score_label.configure(text=f"Score: {self.score}")

        self.current += 1

        self.after(800, self.load_question)

    def show_final_screen(self):

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        final_label = ctk.CTkLabel(
            self.main_frame,
            text="Quiz Finished",
            font=("Arial", 22)
        )
        final_label.pack(pady=20)

        score_label = ctk.CTkLabel(
            self.main_frame,
            text=f"Your score: {self.score} / {len(self.questions)}",
            font=("Arial", 18)
        )
        score_label.pack(pady=10)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = KBCQuiz()
    app.mainloop()