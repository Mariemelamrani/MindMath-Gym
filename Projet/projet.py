import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage, messagebox
import subprocess

def start_game():
    root.withdraw()  # Masquer la fenêtre actuelle
    load_menu_content()

def exit_game():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter le jeu ?"):
        root.destroy()

def show_about():
    # Afficher les informations sur l'utilisation de Sudoku et les rappels sur le temps à respecter
    messagebox.showinfo("About",
                        "Sudoku est un jeu de logique qui consiste à remplir une grille de 9x9 avec des chiffres de 1 à 9.\n\n" 
                        "Règles :\n"
                        "1. Chaque ligne doit contenir tous les chiffres de 1 à 9 sans répétition.\n"
                        "2. Chaque colonne doit contenir tous les chiffres de 1 à 9 sans répétition.\n"
                        "3. Chaque sous-grille de 3x3 doit contenir tous les chiffres de 1 à 9 sans répétition.\n\n"
                        "Rappels sur le temps :\n"
                        "1. Le Sudoku est un jeu qui demande de la concentration.\n"
                        "2. Prenez des pauses régulières pour éviter la fatigue.\n"
                        "3. Fixez-vous une limite de temps pour chaque grille.\n"
                        "4. Amusez-vous bien !"
                        )
    
def back_to_home():
    menu_root.withdraw()  # Masquer la fenêtre du menu
    root.deiconify()  # Afficher la fenêtre principale

def on_button_click1():
    # Action à effectuer lorsque le bouton est cliqué
    subprocess.Popen(["python", "Mental.py"])

def on_button_click2():
    # Action à effectuer lorsque le bouton est cliqué
    subprocess.Popen(["python", "Memorisation.py"])

def on_button_click3():
    # Action à effectuer lorsque le bouton est cliqué
    subprocess.Popen(["python", "Soduko.py"])

def on_button_click():
    # Action à effectuer lorsque le bouton est cliqué
    subprocess.Popen(["python", "Enigme.py"])

def load_menu_content():
    global menu_root
    menu_root = tk.Toplevel(root)  # Créer une nouvelle fenêtre pour le menu
    menu_root.title("Games")
    menu_root.geometry("640x500")
    menu_root.resizable(False, False)
    menu_root.configure(bg="black")

    # Charger l'image à l'aide de PIL pour le logo
    logo_image = Image.open("test.jpg")
    logo_photo = ImageTk.PhotoImage(logo_image)

    # Définir l'image comme icône de la fenêtre principale
    menu_root.iconphoto(False, logo_photo)

    # Charger l'image à l'aide de PIL
    image_icon = Image.open("test.jpg")
    photo_icon = ImageTk.PhotoImage(image_icon)

    # Définir l'image comme icône de la fenêtre principale
    root.iconphoto(True, photo_icon)

    # Charger la première image et redimensionner comme icône
    image1 = Image.open("in.png")
    image1.thumbnail((160, 140))  # Redimensionner l'image pour en faire une icône
    photo1 = ImageTk.PhotoImage(image1)

    # Utiliser l'image dans un widget Label : sudoko
    label1 = tk.Label(menu_root, image=photo1,bg="black")
    label1.place(x=50, y=20)

    # Créer un bouton sous la première image
    button1 = tk.Button(menu_root, text="Enigme", command=on_button_click, font=("Helvetica", 18), bg="#f2f0aa", fg="black", width=10, height=1)
    button1.place(x=50, y=180)

    # Charger la deuxième image et redimensionner comme icône
    image2 = Image.open("sudoku.png")
    image2.thumbnail((150, 140))  # Redimensionner l'image pour en faire une icône
    photo2 = ImageTk.PhotoImage(image2)

    # Utiliser la deuxième image dans un widget Label
    label2 = tk.Label(menu_root, image=photo2,bg="black")
    label2.place(x=250, y=20)

    # Créer un bouton sous la deuxième image
    button2 = tk.Button(menu_root, text="Sudoku", command=on_button_click3, font=("Helvetica", 18), bg="#fcccc2", fg="black", width=10, height=1)
    button2.place(x=250, y=180)

    # Charger la troisième image et redimensionner comme icône
    image3 = Image.open("memorisation.png")
    image3.thumbnail((150, 140))  # Redimensionner l'image pour en faire une icône
    photo3 = ImageTk.PhotoImage(image3)

    # Utiliser la troisième image dans un widget Label
    label3 = tk.Label(menu_root, image=photo3,bg="black")
    label3.place(x=450, y=20)

    # Créer un bouton sous la troisième image
    button3 = tk.Button(menu_root, text="Memorisation", command=on_button_click2, font=("Helvetica", 18), bg="#f2f0aa", fg="black", width=10, height=1)
    button3.place(x=450, y=180)

    image4 = Image.open("cal.png")
    image4.thumbnail((150, 140))  # Redimensionner l'image pour en faire une icône
    photo4 = ImageTk.PhotoImage(image4)

    label4 = tk.Label(menu_root, image=photo4,bg="black")
    label4.place(x=250, y=255)

    # Créer un bouton sous la troisième image
    button4 = tk.Button(menu_root, text="Mental", command=on_button_click1, font=("Helvetica", 18), bg="#fcccc2", fg="black", width=10, height=0)
    button4.place(x=250, y=390)

    # Ajouter le bouton "About"
    about_button = tk.Button(menu_root, text="About", command=show_about,width=8, bg="#83AACD", fg="black", height=1, font=("Helvetica", 12, "italic bold"))
    about_button.place(relx=0.99, rely=0.98, anchor="se")

    start_button = tk.Button(menu_root, text="Back", command=back_to_home , bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
    start_button.place(relx=0.01, rely=0.98, anchor="sw")
    menu_root.mainloop()

# Créer la fenêtre principale
root = tk.Tk()
root.title("My App")
root.geometry("739x410")

# Définition de la couleur de l'arrière-plan
background_color = "#ffffff"  # Blanc

# Création du canevas pour la couleur d'arrière-plan
canvas = tk.Canvas(root, width=1000, height=700, bg=background_color)
canvas.pack()

# Chargement de l'image avec PIL
image_path = Image.open("test.jpg")
image_path.thumbnail((740, 800)) 

# Redimensionnement de l'image
agrandissement = 1
image_resized = image_path.resize((image_path.width * agrandissement, image_path.height * agrandissement))

# Conversion de l'image redimensionnée en PhotoImage
photo_image = ImageTk.PhotoImage(image_resized)

# Création de l'étiquette de fond avec l'image agrandie
bg_image = tk.Label(root, image=photo_image)
bg_image.place(relx=0.5, rely=0.5, anchor="center")

# Création des boutons
start_button = tk.Button(root, text="Start", command=start_game, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
start_button.place(relx=0.99, rely=0.98, anchor="se")

quit_button = tk.Button(root, text="Exit", command=exit_game, bg="#83AACD", fg="black", width=8, height=1, font=("Helvetica", 12, "italic bold"))
quit_button.place(relx=0.01, rely=0.98, anchor="sw")

root.mainloop()
