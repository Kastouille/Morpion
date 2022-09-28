from random import randint
from numpy import matrix
from time import sleep

grille = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

def morpion():
    gagnant = False
    while gagnant == False:
        #Coordonnées:
        ligne = int(input("Veuillez rentrer le numéro de la ligne (1-3)")) - 1
        case = int(input("Veuillez renterer le numéro de la case (1-3)")) - 1
        vider()
        #Placement des pions
        if libre(ligne, case) == True: #Vous
            grille[ligne][case] = "X"
            print(matrix(grille))
            sleep(1)
            vider()
        elif libre(ligne, case) == False:
            print("Cette case est déjà prise !")
        ai_player() #Ordinateur
        print(matrix(grille))
        sleep(1)
        gagnant = gagne()
    return "Le gagnant est", gagnant


def libre(l, c):
    return grille[l][c] == " "

def ai_player():
    ligne = randint(0, 2)
    case = randint(0, 2)
    if libre(ligne, case) == True:
        grille[ligne][case] = "O"
    elif libre(ligne, case) == False:
        ai_player()

def gagne():
    #Lignes horizontales:
    for ligne in grille:
        if ligne == ["X", "X", "X"]:
            return "X"
        elif ligne == ["O", "O", "O"]:
            return "O"

    #Lignes verticales:
    ligne_vert = [[ligne[0] for ligne in grille], [ligne[1] for ligne in grille], [ligne[2] for ligne in grille]]
    for ligne in ligne_vert:
        if ligne == ["X", "X", "X"]:
            return "X"
        elif ligne == ["O", "O", "O"]:
            return "O"

    #Diagonales:
    diago = [[grille[0][0], grille[1][1], grille[2][2]], [grille[0][2], grille[1][1], grille[2][0]]]
    for ligne in diago:
        if ligne == ["X", "X", "X"]:
            return "X"
        elif ligne == ["O", "O", "O"]:
            return "O"

    return False

def vider():
    for i in range(50):
        print(" ")
