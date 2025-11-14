import tkinter as tk
from tkinter import ttk, messagebox
import random
from PIL import Image, ImageTk


class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Mémorisation")
        self.master.geometry("640x500")
        self.master.configure(bg="black")  # Définir l'arrière-plan en noir
        image1 = Image.open("memo.jpeg")
        image1.thumbnail((400, 980))  # Redimensionner l'image pour en faire une icône
        self.photo1 = ImageTk.PhotoImage(image1)
        self.game_frame = None
        self.create_main_page()

    def create_main_page(self):
        self.label_difficulty = tk.Label(self.master, text="Choisissez le niveau de difficulté:",
                                         font=("Helvetica", 12, "italic bold"), bg="black", fg="white")
        self.label_difficulty.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        style = ttk.Style()
        style.configure('TCombobox', fieldbackground='#6da4cf')

        self.difficulty_var = tk.StringVar()
        self.difficulty_combobox = ttk.Combobox(self.master, textvariable=self.difficulty_var,
                                                values=["Facile", "Moyen", "Difficile"],
                                                font=("Helvetica", 12, "italic bold"), style='TCombobox')
        self.difficulty_combobox.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

        self.difficulty_var.set("Facile")

        self.label_sequences = tk.Label(self.master, text="Entrez le nombre de séquences à mémoriser:",
                                        font=("Helvetica", 12, "italic bold"), height=2,bg="black", fg="white")
        self.label_sequences.place(relx=0.5, rely=0.68, anchor=tk.CENTER)

        self.sequence_entry = tk.Entry(self.master, font=("Helvetica", 12, "italic bold"))
        self.sequence_entry.place(relx=0.5, rely=0.74, anchor=tk.CENTER)

        self.start_game_button = tk.Button(self.master, text="Start", command=self.start_game, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        self.start_game_button.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

        self.quit_button = tk.Button(self.master, text="Exit", command=self.master.destroy, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        self.quit_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


        menu_image = Image.open("memo.jpeg")
        menu_photo = ImageTk.PhotoImage(menu_image)

        # Affichage de l'image dans un Label
        menu_image_label = tk.Label(self.master, image=menu_photo, bg="black")
        menu_image_label.place(relx=0.5, rely=0.1, anchor="n")
        menu_image_label.image = menu_photo




        # Assurez-vous que l'image reste en vie




    def start_game(self):
        difficulty = self.difficulty_var.get()
        num_sequences = self.sequence_entry.get()

        if not difficulty or not num_sequences:
            messagebox.showerror("Erreur", "Veuillez saisir le nombre de séquence à mémoriser.")
            return

        self.difficulty = difficulty.lower()
        self.num_sequences = int(num_sequences)
        self.sequence = self.generate_sequence()
        self.current_index = 0
        self.score = 0

        self.create_game_page()

    def generate_sequence(self):
        if self.difficulty == "facile":
            return [str(random.randint(10000, 99999)) for _ in range(self.num_sequences)]
        elif self.difficulty == "moyen":
            return [str(random.randint(1000000, 9999999)) for _ in range(self.num_sequences)]
        elif self.difficulty == "difficile":
            return [str(random.randint(1000000000, 9999999999)) for _ in range(self.num_sequences)]

    def create_game_page(self):
        global menu_root
        for widget in self.master.winfo_children():
            widget.pack_forget()

        self.game_frame = tk.Frame(self.master, bg="black")
        self.game_frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.game_frame, bg="black", fg="white", font=("Helvetica", 12, "italic bold"))
        self.label.place(relx=0.5, rely=0.59, anchor=tk.CENTER)

        self.entry = tk.Entry(self.game_frame, bg="white", fg="black")
        self.entry.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        self.submit_button = tk.Button(self.game_frame, text="Next", command=self.next_number, bg="#6da4cf",
                                       fg="black", font=("Helvetica", 12, "italic bold"),width=8, height=1)
        self.submit_button.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

        self.back_button = tk.Button(self.game_frame, text="Back", command=self.return_to_main_page,
                                     bg="#6da4cf", fg="black", width=8, height=1,font=("Helvetica", 12, "italic bold"))
        self.back_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

        label_image = tk.Label(self.game_frame, image=self.photo1, bg="black")
        label_image.place(relx=0.5, rely=0.1, anchor="n")

        self.display_next_number()
        menu_root.mainloop()

    def display_next_number(self):
        if self.current_index < len(self.sequence):
            number = self.sequence[self.current_index]
            self.label.config(text=number)
            self.master.after(3000, lambda: self.clear_label_and_entry())
        else:
            self.show_score_message()

    def clear_label_and_entry(self):
        self.label.config(text="")
        self.entry.delete(0, tk.END)

    def next_number(self):
        if self.current_index < len(self.sequence):
            entered_number = self.entry.get()
            correct_number = self.sequence[self.current_index]
            if entered_number == correct_number:
                self.score += 1
            self.current_index += 1
            self.display_next_number()
            self.entry.delete(0, tk.END)

    def show_score_message(self):
        correct_answers = self.score
        total_sequences = self.num_sequences
        score_text = f"Votre score est de : {correct_answers} / {total_sequences}"
        messagebox.showinfo("Fin du jeu", score_text)
        self.game_frame.destroy()
        self.create_main_page()

    def return_to_main_page(self):
        self.game_frame.destroy()
        self.create_main_page()


def main():
    root = tk.Tk()
    root.title("Jeu de Mémorisation")
    root.geometry("640x500")
    root.configure(bg="black")
    game = MemoryGame(root)
    icon_image = tk.PhotoImage(file="memo.png")
    root.iconphoto(False, icon_image)
    # Définir l'icône de la fenêtre
   

    root.mainloop()


if __name__ == "__main__":
    main()
