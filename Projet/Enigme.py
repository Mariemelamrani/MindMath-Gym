import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
from PIL import Image, ImageTk


class JeuEnigmeMath(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jeu d'Énigme Mathématique")
        self.configure(background='black')
        self.geometry("900x500")
        self.resizable(False,False)
        self.icon = Image.open("memo.png")  # Charger l'icône
        self.icon.thumbnail((32, 32))  # Redimensionner l'icône
        self.icon = ImageTk.PhotoImage(self.icon)  # Convertir l'icône en format Tkinter
        self.iconphoto(True, self.icon)  # Définir l'icône de la fenêtre

        image1 = Image.open("Enigme.jpg")
        image1.thumbnail((400, 980))  # Redimensionner l'image pour en faire une icône
        self.photo1 = ImageTk.PhotoImage(image1)
        self.difficulty = tk.StringVar()
        self.difficulty.set("Facile")
        self.problems = []
        self.create_widgets_menu()

    def create_widgets_menu(self):
        self.label_difficulty = tk.Label(self, text="Choisissez le niveau de difficulté :", fg="white" ,bg="black",width=51, height=2,
                                         font=("Helvetica", 12, "italic bold"))
        self.label_difficulty.place(relx=0.5, rely=0.18, anchor=tk.CENTER)
        self.combobox_difficulty = ttk.Combobox(self, textvariable=self.difficulty,
                                                values=["Facile", "Moyen", "Difficile"], height=2, width=14,
                                                font=("Helvetica", 12, "italic bold"))
        self.combobox_difficulty.place(relx=0.5, rely=0.23, anchor="center")

        self.combobox_difficulty.set("Facile")

        self.label_problems = tk.Label(self, text="Choisissez le nombre de problèmes :", fg="white" ,bg="black",height=2, width=51,
                                       font=("Helvetica", 12, "italic bold"))
        self.label_problems.place(relx=0.5, rely=0.38, anchor="center")
        self.problems_var = tk.IntVar()
        self.problems_var.set(1)
        self.entry_problems = tk.Entry(self, textvariable=self.problems_var, width=8,
                                       font=("Helvetica", 12, "italic bold"))
        self.entry_problems.place(relx=0.5, rely=0.45, anchor="center")

        self.button_start = tk.Button(self, text="Start", command=self.commencer_jeu, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        self.button_start.place(relx=0.99, rely=1, anchor="se")

        self.button_quit = tk.Button(self, text="Exit", command=self.destroy, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        self.button_quit.place(relx=0.01, rely=1, anchor="sw")

        # Ajouter l'image dans le menu
        label_image = tk.Label(self, image=self.photo1,bg="black")
        label_image.place(relx=0.5, rely=0.9, anchor="s")

    # Les autres méthodes restent inchangées...

    def commencer_jeu(self):
        self.problems = self.generer_problemes()
        if self.problems:
            self.create_widgets_jeu()
        else:
            messagebox.showerror("Erreur", "Aucun problème généré. Veuillez choisir un niveau de difficulté et un nombre de problèmes valide.")

    def generer_problemes(self):
        problems_facile = [
            ("Dans dix ans, j'aurai deux fois l'âge de mon frère. La somme de nos âges sera alors : 45 ans. Quel est mon âge maintenant ?", "25", ["15", "25", "35", "45"]),
            ("Un nombre est multiplié par 5, puis on ajoute 6 au résultat. Si on obtient 21, quel est le nombre de départ ?", "3", ["3", "4", "5", "6"]),
            ("Si on additionne 5 à un nombre, puis on multiplie le résultat par 4, on obtient 36. Quel est le nombre de départ ?", "8", ["6", "7", "8", "9"]),
            ("Le produit de 7 par un nombre est égal à 49. Quel est ce nombre ?", "7", ["6", "7", "8", "9"]),
            ("Si on multiplie un nombre par 8, puis on soustrait 4 au résultat, on obtient 20. Quel est le nombre de départ ?", "3", ["2", "3", "4", "5"]),
            ("La somme de deux nombres est 15. Si l'un des nombres est 7, quel est l'autre ?", "8", ["6", "7", "8", "9"]),
            ("Si on divise un nombre par 4, puis on ajoute 5 au résultat, on obtient 12. Quel est le nombre de départ ?", "43", ["38", "39", "43", "44"]),
            ("Si on soustrait 8 à un nombre, puis on multiplie le résultat par 6, on obtient 54. Quel est le nombre de départ ?", "11", ["11", "12", "13", "14"]),
            ("Si on multiplie un nombre par 7, puis on ajoute 5 au résultat, on obtient 26. Quel est le nombre de départ ?", "3", ["2", "3", "4", "5"]),
            ("La somme de trois nombres est 50. Si l'un des nombres est 18 et un autre est 12, quel est le troisième ?", "20", ["20", "22", "24", "26"]),
            ("Si on multiplie un nombre par 9, puis on divise le résultat par 3, on obtient 27. Quel est le nombre de départ ?", "9", ["6", "9", "12", "15"]),
            ("Si on soustrait 5 à un nombre, puis on multiplie le résultat par 7, on obtient 42. Quel est le nombre de départ ?", "7", ["6", "7", "8", "9"]),
            ("La somme de deux nombres est 35. Si l'un des nombres est 17, quel est l'autre ?", "18", ["18", "19", "20", "21"])
        ]

        problems_moyen = [
            ("Dans cinq ans, l'âge d'Antoine sera le triple de celui qu'il avait il y a cinq ans. Quel est l'âge d'Antoine ?", "10", ["5", "7", "10", "12"]),
            ("La somme de deux nombres est 72. Si l'un des nombres est 32, quel est l'autre ?", "40", ["35", "40", "45", "50"]),
            ("La différence de deux nombres est 12. Si l'un des nombres est 24, quel est l'autre ?", "36", ["32", "36", "40", "44"]),
            ("Si on multiplie un nombre par 4, puis on ajoute 7 au résultat, on obtient 39. Quel est le nombre de départ ?", "8", ["7", "8", "9", "10"]),
            ("La somme de deux nombres est 86. Si l'un des nombres est 39, quel est l'autre ?", "47", ["44", "47", "50", "53"]),
            ("La différence de deux nombres est 16. Si l'un des nombres est 32, quel est l'autre ?", "16", ["12", "16", "20", "24"]),
            ("Si on divise un nombre par 3, puis on ajoute 8 au résultat, on obtient 22. Quel est le nombre de départ ?", "42", ["36", "42", "48", "54"]),
            ("Si on soustrait 6 à un nombre, puis on divise le résultat par 5, on obtient 9. Quel est le nombre de départ ?", "55", ["50", "55", "60", "65"]),
            ("La somme de trois nombres est 126. Si l'un des nombres est 52 et un autre est 34, quel est le troisième ?", "40", ["38", "40", "42", "44"]),
            ("La différence de deux nombres est 18. Si l'un des nombres est 27, quel est l'autre ?", "45", ["36", "45", "54", "63"]),
            ("Si on multiplie un nombre par 7, puis on soustrait 9 au résultat, on obtient 50. Quel est le nombre de départ ?", "7", ["5", "7", "9", "11"]),
            ("Si on soustrait 8 à un nombre, puis on multiplie le résultat par 6, on obtient 54. Quel est le nombre de départ ?", "11", ["10", "11", "12", "13"]),
            ("La somme de deux nombres est 64. Si l'un des nombres est 25, quel est l'autre ?", "39", ["36", "39", "42", "45"])
        ]

        problems_difficile = [
            ("Dans dix ans, l'âge de Thomas sera le double de celui qu'il avait il y a dix ans. Quel est l'âge de Thomas ?", "30", ["20", "25", "30", "35"]),
            ("La somme de trois nombres est 120. Si l'un des nombres est 40 et un autre est 25, quel est le troisième ?", "55", ["50", "55", "60", "65"]),
            ("La différence de deux nombres est 24. Si l'un des nombres est 48, quel est l'autre ?", "24", ["22", "24", "26", "28"]),
            ("Si on multiplie un nombre par 8, puis on soustrait 12 au résultat, on obtient 52. Quel est le nombre de départ ?", "8", ["6", "8", "10", "12"]),
            ("La somme de deux nombres est 96. Si l'un des nombres est 37, quel est l'autre ?", "59", ["54", "59", "64", "69"]),
            ("La différence de deux nombres est 32. Si l'un des nombres est 56, quel est l'autre ?", "24", ["20", "24", "28", "32"]),
            ("Si on divise un nombre par 4, puis on ajoute 11 au résultat, on obtient 32. Quel est le nombre de départ ?", "84", ["72", "84", "96", "108"]),
            ("Si on soustrait 7 à un nombre, puis on divise le résultat par 5, on obtient 11. Quel est le nombre de départ ?", "60", ["55", "60", "65", "70"]),
            ("La somme de trois nombres est 210. Si l'un des nombres est 85 et un autre est 54, quel est le troisième ?", "71", ["65", "71", "77", "83"]),
            ("La différence de deux nombres est 40. Si l'un des nombres est 58, quel est l'autre ?", "18", ["14", "18", "22", "26"]),
            ("Si on multiplie un nombre par 9, puis on soustrait 15 au résultat, on obtient 78. Quel est le nombre de départ ?", "9", ["6", "9", "12", "15"]),
            ("Si on soustrait 9 à un nombre, puis on multiplie le résultat par 6, on obtient 60. Quel est le nombre de départ ?", "11", ["10", "11", "12", "13"]),
            ("La somme de deux nombres est 168. Si l'un des nombres est 63, quel est l'autre ?", "105", ["98", "105", "112", "119"])
        ]

        difficulty = self.difficulty.get()
        if difficulty == "Facile":
            return random.sample(problems_facile, self.problems_var.get())
        elif difficulty == "Moyen":
            return random.sample(problems_moyen, self.problems_var.get())
        elif difficulty == "Difficile":
            return random.sample(problems_difficile, self.problems_var.get())
        else:
            return []

    def create_widgets_jeu(self):
        self.destroy_menu_widgets()

        self.current_problem_index = 0
        self.score = 0
        self.temps_debut = time.time()
        self.temps_total = 60  # Temps total en secondes pour chaque opération

        self.label_question = tk.Label(self, text="", font=("Helvetica", 12, "italic bold"), fg="white",bg="black")
        self.label_question.place(relx=0.5, rely=0.19, anchor="center")

        self.combobox_reponses = ttk.Combobox(self,width=34,height=3)
        self.combobox_reponses.place(relx=0.5, rely=0.27, anchor=tk.CENTER)

        self.button_suivant = tk.Button(self, text="Next",command=self.question_suivante, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        self.button_suivant.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

        self.label_temps = tk.Label(self, text="Temps restant: 60",width=26,height=2,fg="white",bg="black",font=("Helvetica", 12, "italic bold"))
        self.label_temps.place(relx=0.5, rely=0.44, anchor=tk.CENTER)

        self.button_retour_menu = tk.Button(self, text="Back", command=self.retour_menu, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
        self.button_retour_menu.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

        self.maj_question()
        self.update_temps_restant()


    def destroy_menu_widgets(self):
        self.label_difficulty.destroy()
        self.combobox_difficulty.destroy()
        self.label_problems.destroy()
        self.entry_problems.destroy()
        self.button_start.destroy()
        self.button_quit.destroy()

    def destroy_jeu_widgets(self):
        self.label_question.destroy()
        self.combobox_reponses.destroy()
        self.button_suivant.destroy()
        self.label_temps.destroy()
        self.button_retour_menu.destroy()

    def maj_question(self):
        if self.current_problem_index < len(self.problems):
            problem, _, choices = self.problems[self.current_problem_index]
            self.label_question.config(text=problem)
            self.combobox_reponses.set('')  # Réinitialiser la combobox
            self.combobox_reponses['values'] = choices
            self.reponse_correcte = _
        else:
            self.fin_jeu()

    def question_suivante(self):
        reponse_utilisateur = self.combobox_reponses.get()
        if reponse_utilisateur == self.reponse_correcte:
            self.score += 1
        self.current_problem_index += 1
        self.maj_question()
        self.temps_debut = time.time()  # Réinitialiser le temps de début
        self.update_temps_restant()

    def retour_menu(self):
        self.destroy_jeu_widgets()
        self.create_widgets_menu()

    def update_temps_restant(self):
        temps_ecoule = round(time.time() - self.temps_debut)
        temps_restant = max(self.temps_total - temps_ecoule, 0)
        minutes = temps_restant // 60
        secondes = temps_restant % 60
        self.label_temps.config(text=f"Temps restant: {minutes:02}:{secondes:02}")

        if temps_restant > 0:  # Continuer la mise à jour tant que le temps n'est pas écoulé
            self.after(1000, self.update_temps_restant)
        else:
            self.question_suivante()  # Passer à la question suivante lorsque le temps est écoulé

    def fin_jeu(self):
        temps_total = round(time.time() - self.temps_debut)
        messagebox.showinfo("Fin du jeu", f"Votre score est de {self.score}/{len(self.problems)} en {temps_total} secondes.")
        self.destroy_jeu_widgets()
        self.create_widgets_menu()

if __name__ == "__main__":
    app = JeuEnigmeMath()
    app.mainloop()

