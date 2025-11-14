import tkinter as tk
from tkinter import messagebox, ttk
import random
import time
from PIL import Image, ImageTk


class SudokuGame:
    def __init__(self, root):
        self.root = root
        root.geometry("700x500")
        root.resizable(False, False)
        root.configure(bg="black", width=10)  # Définition de la couleur de fond
        image1 = Image.open("sodoko.png")
        image1.thumbnail((400, 980))  # Redimensionner l'image pour en faire une icône
        self.photo1 = ImageTk.PhotoImage(image1)
        self.root.title("Sudoku")
        self.difficulty = tk.StringVar()
        self.difficulty.set("Facile")
        self.create_main_menu()
        self.attempts = 0
        self.base_score = 0  # Variable pour stocker le score initial
        self.score = self.base_score  # Score actuel

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Ajouter des marges aux cadres des menus et les séparer un peu
        menu_frame = tk.Frame(self.root, bg="black", bd=5, relief="raised", padx=10, pady=10 )
        menu_frame.pack(side="bottom", fill="both", expand=True)

        tk.Label(menu_frame, text="Choisissez le niveau de difficulté :", bg="black", fg="white" ,  width=31, height=2,font=("Helvetica",12,"italic bold")).place(relx=0.5,rely=0.22,anchor=tk.CENTER)

        # Placer la combobox
        combobox = ttk.Combobox(menu_frame, textvariable=self.difficulty, values=["Facile", "Moyen", "Difficile"] ,  width=11, height=2 , font=("Helvetica",12,"italic bold") )
        combobox.place(relx=0.5, rely=0.4, anchor="center")

        # Placer les boutons
        start_button = tk.Button(menu_frame, text="Start", command=self.start_game, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        start_button.place(relx=1, rely=1, anchor="se")  # Commencer en bas à droite

        quit_button = tk.Button(menu_frame, text="Exit", command=self.quit_game , bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        quit_button.place(relx=0, rely=1, anchor="sw")  # Quitter en bas à gauche


        # Ajouter des marges à l'image
        image_frame = tk.Frame(self.root, padx=10, pady=10 , bg="black")  # Frame pour l'image
        image_frame.pack(side="top", fill="both", expand=True)

        label_image = tk.Label(image_frame, image=self.photo1 , bg="black")
        label_image.place(relx=0.5, rely=0.53, anchor="center")

    def quit_game(self):
        self.root.destroy()

    def create_board(self):
        base = 3
        side = base * base

        def pattern(r, c):
            return (base * (r % base) + r // base + c) % side

        def shuffle(s):
            return random.sample(s, len(s))

        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base * base + 1))

        board = [[nums[pattern(r, c)] for c in cols] for r in rows]

        squares = side * side
        difficulty = self.difficulty.get()
        if difficulty == "Facile":
            empties = squares * 4 // 9
        elif difficulty == "Moyen":
            empties = squares * 6 // 9
        else:
            empties = squares * 7 // 9

        self.solution = [[0] * 9 for _ in range(9)]
        for p in random.sample(range(squares), empties):
            self.solution[p // side][p % side] = board[p // side][p % side]
            board[p // side][p % side] = 0

        return board

    def start_game(self):
        self.start_time = time.time()
        self.board = self.create_board()
        self.display_board()

    def display_board(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

        # Cadre pour les nombres
        numbers_frame = tk.Frame(self.root, bg="#0b0475", bd=5)
        numbers_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.entries = []
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(numbers_frame, width=3, font=('Arial', 16, 'bold'))
                entry.grid(row=i, column=j, padx=2, pady=2)
                if self.board[i][j] != 0:
                    entry.insert(tk.END, str(self.board[i][j]))
                    entry.config(state=tk.DISABLED)
                self.entries.append(entry)

                if (i + 1) % 3 == 0 and i != 8:
                    entry.grid(pady=(0, 5))
                if (j + 1) % 3 == 0 and j != 8:
                    entry.grid(padx=(0, 5))

        # Cadre pour les boutons
        buttons_frame = tk.Frame(self.root, bg="black", bd=5)
        buttons_frame.place(relx=0.5, rely=0.87, anchor="center")

        check_button = tk.Button(buttons_frame, text="Check", command=self.check_solution,bg="#aaa7d4")
        check_button.grid(row=0, column=0, padx=5, pady=5)

        new_game_button = tk.Button(buttons_frame, text="New Game", command=self.start_game,bg="#4034ed")
        new_game_button.grid(row=0, column=1, padx=5, pady=5)

        return_button = tk.Button(buttons_frame, text="Back", command=self.create_main_menu,bg="#aaa7d4")
        return_button.grid(row=0, column=2, padx=5, pady=5)

        clear_button = tk.Button(buttons_frame, text="Clear All", command=self.clear_all,bg="#4034ed")
        clear_button.grid(row=0, column=3, padx=5, pady=5)

        solution_button = tk.Button(buttons_frame, text="Solution", command=self.fill_solution,bg="#aaa7d4")
        solution_button.grid(row=0, column=4, padx=5, pady=5)

        # Cadre pour l'affichage de la minuterie et du score
        timer_score_frame = tk.Frame(self.root, bg="black")
        timer_score_frame.place(relx=0.5, rely=0.96, anchor="center")

        self.timer_label = tk.Label(timer_score_frame, text="Temps restant : 10:00")
        self.timer_label.grid(row=0, column=0, padx=10, pady=16 )

        self.score_label = tk.Label(timer_score_frame, text=f"Score : {self.score}")
        self.score_label.grid(row=0, column=1, padx=10, pady=21)

        self.update_timer()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, 600 - elapsed_time)
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        self.timer_label.config(text=f"Temps restant : {minutes:02d}:{seconds:02d}")

        if remaining_time > 0:
            self.root.after(1000, self.update_timer)

    def check_solution(self):
        user_solution = []
        for entry in self.entries:
            value = entry.get()
            if value == "":
                value = "0"
            if not value.isdigit() or int(value) < 0 or int(value) > 9:
                messagebox.showerror("Sudoku", "Veuillez entrer des chiffres de 0 à 9.")
                return
            user_solution.append(int(value))
        if self.is_valid_solution(user_solution):
            elapsed_time = time.time() - self.start_time
            self.score += 1  # Augmenter le score après chaque résolution réussie
            self.update_score_label()
            messagebox.showinfo("Sudoku", f"Félicitations! Vous avez résolu le Sudoku en {elapsed_time:.2f} secondes.")
            self.start_game()  # Redémarrer le jeu
        else:
            messagebox.showerror("Sudoku", "La solution proposée est incorrecte. Veuillez réessayer.")
            self.highlight_errors()

    def update_score_label(self):
        self.score_label.config(text=f"Score : {self.score}")

    def is_valid_solution(self, solution):
        if len(solution) != 81:
            return False

        def is_valid_group(group):
            return len(set(group)) == 9 and all(1 <= x <= 9 for x in group)

        rows = [solution[i:i + 9] for i in range(0, 81, 9)]
        cols = [[solution[i + j * 9] for j in range(9)] for i in range(9)]
        squares = [[solution[i + j + k * 9] for j in range(3) for k in range(3)] for i in range(0, 81, 27)]

        return all(is_valid_group(row) for row in rows) and \
               all(is_valid_group(col) for col in cols) and \
               all(is_valid_group(square) for square in squares)

    def clear_all(self):
        for entry in self.entries:
            if entry['state'] != tk.DISABLED:
                entry.delete(0, tk.END)

    def fill_solution(self):
        for i in range(9):
            for j in range(9):
                entry = self.entries[i * 9 + j]
                if entry.get() == "":
                    entry.insert(tk.END, str(self.solution[i][j]))
                elif entry.get() != str(self.solution[i][j]):
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, str(self.solution[i][j]))


root = tk.Tk()
icon_image = tk.PhotoImage(file="memo.png")
root.iconphoto(False, icon_image)
game = SudokuGame(root)
root.mainloop()
