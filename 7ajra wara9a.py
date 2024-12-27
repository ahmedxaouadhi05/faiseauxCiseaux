import tkinter as tk
import random

# Fonction pour générer le choix de l'ordinateur
def computer_choice():
    return random.choice(["Pierre", "Feuille", "Ciseaux"])

# Fonction pour déterminer le gagnant
def determine_winner(user, computer):
    if user == computer:
        return "Égalité"
    elif (user == "Pierre" and computer == "Ciseaux") or \
         (user == "Feuille" and computer == "Pierre") or \
         (user == "Ciseaux" and computer == "Feuille"):
        return "Vous gagnez!"
    else:
        return "L'ordinateur gagne!"

# Fonction pour mettre à jour le jeu et afficher les résultats
def play_game(user_choice):
    comp_choice = computer_choice()
    result = determine_winner(user_choice, comp_choice)
    
    # Affichage du choix de l'ordinateur et du résultat
    result_label.config(text=f"Ordinateur a choisi: {comp_choice}\n{result}")
    
    # Mise à jour du score
    if result == "Vous gagnez!":
        user_score.set(user_score.get() + 1)
    elif result == "L'ordinateur gagne!":
        computer_score.set(computer_score.get() + 1)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Pierre, Feuille, Ciseaux")

# Variables pour les scores
user_score = tk.IntVar(value=0)
computer_score = tk.IntVar(value=0)

# Affichage des scores
score_label = tk.Label(root, text="Scores", font=("Arial", 14))
score_label.pack(pady=10)

score_display = tk.Label(root, text="Joueur: 0 | Ordinateur: 0", font=("Arial", 12))
score_display.pack(pady=10)

# Fonction pour mettre à jour les scores
def update_scores():
    score_display.config(text=f"Joueur: {user_score.get()} | Ordinateur: {computer_score.get()}")

# Boutons pour faire un choix
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

pierre_button = tk.Button(button_frame, text="Pierre", font=("Arial", 14), command=lambda: play_game("Pierre"))
pierre_button.grid(row=0, column=0, padx=10)

feuille_button = tk.Button(button_frame, text="Feuille", font=("Arial", 14), command=lambda: play_game("Feuille"))
feuille_button.grid(row=0, column=1, padx=10)

ciseaux_button = tk.Button(button_frame, text="Ciseaux", font=("Arial", 14), command=lambda: play_game("Ciseaux"))
ciseaux_button.grid(row=0, column=2, padx=10)

# Affichage du résultat du jeu
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Bouton pour réinitialiser le jeu
reset_button = tk.Button(root, text="Réinitialiser le jeu", font=("Arial", 12), command=lambda: [user_score.set(0), computer_score.set(0), update_scores(), result_label.config(text="")])
reset_button.pack(pady=20)

# Lancer l'interface
root.mainloop()
