#   __  __                  _             
#  |  \/  |                (_)            
#  | \  / | ___  _ __ _ __  _  ___  _ __  
#  | |\/| |/ _ \| '__| '_ \| |/ _ \| '_ \ 
#  | |  | | (_) | |  | |_) | | (_) | | | |
#  |_|  |_|\___/|_|  | .__/|_|\___/|_| |_|
#                    | |                  
#                    |_|     

from random import randint
from numpy import matrix
from time import sleep

grille = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

def morpion():
    """
    Le jeu du morpion dans la console Python, avec un joueur AI.
    Amusez-vous à jouer au morpion contre l'ordinateur !
    (Relancez le programme à chaque fin de partie pour réinitialiser les variables)
    Syntaxe :
        morpion() --> Le jeu commence
    """
    gagnant = False
    mouvements = 0
    while gagnant == False:
        #Coordonnées du joueur:
        ligne = int(input("Veuillez rentrer le numéro de la ligne (1-3)")) - 1
        case = int(input("Veuillez renterer le numéro de la case (1-3)")) - 1
        vider()
        #Placement des pions
        if libre(ligne, case) == True: #Vous
            grille[ligne][case] = "X"
            mouvements += 1
            print(matrix(grille))
            sleep(1)
            vider()
        elif libre(ligne, case) == False:
            print("Cette case est déjà prise, veuillez reccomencer !")
            continue
        ai_player() #Ordinateur
        mouvements += 1
        print(matrix(grille))
        sleep(1)
        gagnant = gagne(mouvements)
    vider()
    return "Gagnant :", gagnant


def libre(l, c):
    #Vérifie si la case est libre
    return grille[l][c] == " "

def ai_player():
    #Joueur automatique
    ligne = randint(0, 2)
    case = randint(0, 2)
    if libre(ligne, case) == True:
        grille[ligne][case] = "O"
    elif libre(ligne, case) == False:
        ai_player()

def gagne(m):
    #Vérifie si les conditions de victoires sont réunies
    #et pour quel joueur, retourne le gagnant
    
    #Lignes horizontales:
    for ligne in grille:
        if ligne == ["X", "X", "X"]:
            return "Vous"
        elif ligne == ["O", "O", "O"]:
            return "Ordinateur"

    #Lignes verticales:
    ligne_vert = [[ligne[0] for ligne in grille], [ligne[1] for ligne in grille], [ligne[2] for ligne in grille]]
    for ligne in ligne_vert:
        if ligne == ["X", "X", "X"]:
            return "Vous"
        elif ligne == ["O", "O", "O"]:
            return "Ordinateur"

    #Diagonales:
    diago = [[grille[0][0], grille[1][1], grille[2][2]], [grille[0][2], grille[1][1], grille[2][0]]]
    for ligne in diago:
        if ligne == ["X", "X", "X"]:
            return "Vous"
        elif ligne == ["O", "O", "O"]:
            return "Ordinateur"
    
    #Match nul:
    if m == 9:
        return "Aucun, match nul !"
    
    #Aucune condition remplie
    return False

def vider():
    #Vide l'écran entre chaque mouvements
    for i in range(50):
        print(" ")
