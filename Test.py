import tkinter as tk

def lettre_click(nouvelle_lettre):
    global lettre
    lettre = nouvelle_lettre
    print(f'Lettre sélectionnée : {lettre}')

# Crée une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Sélection de lettre")

# Variable pour stocker la lettre sélectionnée
lettre = None

# Crée des boutons pour chaque lettre de l'alphabet et associe la fonction de rappel lettre_click
for lettre in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    bouton = tk.Button(fenetre, text=lettre, command=lambda l=lettre: lettre_click(l))
    bouton.pack()

# Lance la boucle principale de l'application
fenetre.mainloop()
