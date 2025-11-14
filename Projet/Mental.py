import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

class CalculMentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcul Mental")
        self.root.geometry("640x500")
        self.root.configure(bg="black")
        self.jeu_frame = None  # Initialize jeu_frame attribute
        self.score_label = tk.Label(self.root, text="", bg="black", fg="white")
        self.chrono_label = tk.Label(self.root, text="", font=("Helvetica", 9), bg="black", fg="white")
        self.operation_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="black", fg="white")
        self.entry = None
        self.suivant_button = None
        self.back_button = None
        self.score = 0  # Initialize score attribute
        self.total_operations = []  # Initialize total_operations attribute
        self.current_operation_index = 0  # Initialize current_operation_index attribute
        self.score_affiche = False  # Initialize score display control variable
        self.chrono_en_cours = False  # Initialize chrono control variable

        self.create_widgets()

    def create_widgets(self):
        # Charger l'image et redimensionner comme icône
        image3 = Image.open("calcul.png")
        image3.thumbnail((200, 190))  # Redimensionner l'image pour en faire une icône
        self.photo3 = ImageTk.PhotoImage(image3)  # Conserver une référence à l'image

        # Utiliser l'image dans un widget Label
        label3 = tk.Label(image=self.photo3, bg="black")
        label3.pack()

        tk.Label(self.root, text="Choisissez le niveau :", bg="black", fg="white", font=("Helvetica", 12, "italic bold")).place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        self.niveaux = ["Facile", "Moyen", "Difficile"]
        self.niveau_combobox = ttk.Combobox(self.root, values=self.niveaux)
        self.niveau_combobox.current(0)
        self.niveau_combobox.place(relx=0.5,rely=0.56,anchor=tk.CENTER)

        tk.Label(self.root, text="Entrez le nombre d'opérations :", bg="black", fg="white", font=("Helvetica", 12, "italic bold")).place(relx=0.5,rely=0.68,anchor=tk.CENTER)
        self.nb_operations_entry = tk.Entry(self.root, bg="black", fg="white")
        self.nb_operations_entry.place(relx=0.5,rely=0.74,anchor=tk.CENTER)

        # Placer le bouton Quitter à gauche
        quitter_button = tk.Button(self.root, text="Exit", command=self.root.destroy, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        quitter_button.place(relx=0.01,rely=1,anchor="sw")

        # Placer le bouton Commencer à droite
        commencer_button = tk.Button(self.root, text="Start", command=self.commencer, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        commencer_button.place(relx=0.99,rely=1,anchor="se")




    def commencer(self):
        niveau = self.niveau_combobox.get()
        nb_operations = int(self.nb_operations_entry.get())
        self.total_operations = self.generer_operations(niveau, nb_operations)
        self.current_operation_index = 0

        self.score_affiche = False  # Réinitialiser la variable de contrôle du score affiché
        self.score = 0  # Réinitialiser le score

        # Masquer les widgets de la configuration
        for widget in self.root.winfo_children():
            widget.pack_forget()

        # Afficher les widgets du jeu
        self.create_jeu_frame()

        self.operation_label.config(text=self.total_operations[self.current_operation_index])
        self.entry.delete(0, tk.END)  # Effacer le contenu de l'entrée existante
        self.remaining_time = 20
        self.start_chrono()

    def create_jeu_frame(self):
        
        
        self.jeu_frame = tk.Frame(self.root, bg="black")

        # Centrer le frame de jeu verticalement
        self.jeu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Votre code existant pour les autres widgets...


        #Charger l'image et redimensionner comme icône
        image3 = Image.open("calcul.png")
        image3.thumbnail((200, 190))  # Redimensionner l'image pour en faire une icône
        photo3 = ImageTk.PhotoImage(image3)

        # Utiliser l'image dans un widget Label
        label3 = tk.Label(self.jeu_frame, image=photo3, bg="black")
        label3.image = photo3  # Gardez une référence à l'image pour éviter la collecte des déchets
        label3.place(relx=0.5, rely=0.3, anchor="n")

        self.operation_label.pack()
        

        self.entry = tk.Entry(self.jeu_frame)
        self.entry.place(relx=0.5,rely=0.05,anchor="center")
        
        self.chrono_label.pack()

        self.suivant_button = tk.Button(self.jeu_frame, text="Next", command=self.operation_suivante, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        self.suivant_button.place(relx=0.99,rely=1,anchor="se")

        self.back_button = tk.Button(self.jeu_frame, text="Back", command=self.return_to_main_page, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        self.back_button.place(relx=0.01,rely=1,anchor="sw")

        self.jeu_frame.pack(expand=True, fill=tk.BOTH)
        

        # Réinitialiser la variable de contrôle du score affiché
        self.score_affiche = False

       

        self.operation_label.pack()

        self.entry.delete(0, tk.END)  # Effacer le contenu de l'entrée existante

        self.remaining_time = 20
        self.start_chrono()
        

    def start_chrono(self):
        if not self.chrono_en_cours:
            self.chrono_en_cours = True
            self.update_chrono()

    def update_chrono(self):
        if self.remaining_time >= 0:
            self.chrono_label.config(text=f"Temps restant : {self.remaining_time}")
            self.remaining_time -= 1
            self.root.after(1000, self.update_chrono)
        else:
            self.chrono_en_cours = False
            self.operation_suivante()

    def operation_suivante(self):
        if self.current_operation_index < len(self.total_operations):
            operation = self.total_operations[self.current_operation_index]
            reponse = self.entry.get().strip()
            if not reponse:  # Vérifier si la réponse est vide
                reponse = None
            try:
                if reponse is None or (reponse.isdigit() and int(reponse) == eval(operation)):
                    if reponse is not None:  # Incrémenter le score uniquement si la réponse n'est pas vide
                        self.score += 1
            except ValueError:
                pass  # Ignore les erreurs de conversion en entier

            self.current_operation_index += 1

            if self.current_operation_index < len(self.total_operations):
                self.operation_label.config(text=self.total_operations[self.current_operation_index])
                self.entry.delete(0, tk.END)
                self.remaining_time = 20
                self.start_chrono()
            else:
                self.afficher_score()
        else:
            self.afficher_score()

    def create_game_widgets(self):
        self.jeu_frame = tk.Frame(self.root, bg="black")

        # Calculate y position to center the frame vertically
        window_height = self.root.winfo_height()
        frame_height = 200  # Adjust this value as needed
        y_position = (window_height - frame_height) // 2

        # Place the frame at the calculated y position
        self.jeu_frame.place(relx=0.5, rely=y_position / window_height, anchor=tk.CENTER)

        self.operation_label.pack()
        self.entry.pack()
        self.chrono_label.pack()
        self.suivant_button.pack(side=tk.RIGHT)
        self.back_button.pack(side=tk.LEFT)








    def hide_game_widgets(self):
        self.jeu_frame.pack_forget()
        self.operation_label.pack_forget()
        self.entry.pack_forget()
        self.suivant_button.pack_forget()
        self.back_button.pack_forget()
        self.chrono_label.pack_forget()

    def return_to_main_page(self):
        # Masquer les widgets du jeu
        self.hide_game_widgets()

        # Afficher à nouveau les widgets de la configuration
        self.create_widgets()

    def afficher_score(self):
        if not self.score_affiche:
            self.score_affiche = True
            score_text = f"Votre score est : {self.score}/{len(self.total_operations)}"
            messagebox.showinfo("Score", score_text)
            self.return_to_main_page()

    def generer_operations(self, niveau, nb_operations):
        operations = []
        for _ in range(nb_operations):
            if niveau == "Facile":
                operation = self.generer_operation_facile()
            elif niveau == "Moyen":
                operation = self.generer_operation_moyen()
            elif niveau == "Difficile":
                operation = self.generer_operation_difficile()

            if operation is not None:
                operations.append(operation)
        return operations

    def generer_operation_facile(self):
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        operateur = random.choice(["+", "*"])
        return f"{a} {operateur} {b}"

    def generer_operation_moyen(self):
        a = random.randint(100, 999)
        b = random.randint(100, 999)
        operateur = random.choice(["+", "-", "*"])
        return f"{a} {operateur} {b}"

    def generer_operation_difficile(self):
        a = random.randint(1000, 9999)
        b = random.randint(1000, 9999)
        operateur = random.choice(["+", "-", "*", "/"])
        return f"{a} {operateur} {b}"

root = tk.Tk()
icon_image = tk.PhotoImage(file="memo.png")
root.iconphoto(False, icon_image)
app = CalculMentalApp(root)
root.mainloop()


 


