print("Bienvenue dans le jeu du Morpion ! À l'aide de ton clavier choisi un nombre entre 1 et 9 pour selectionné un emplacement vide.\n\
Le 1er joueur qui reussi à alligné trois X ou O est le gagnant ! Bonne chance. \n\
Le joueur 'X'commence :") #Introduction 


#initialisation
grille = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

currentPlayer = "X" #Variable qui détermine le joueur actuel (commence par "X").
gameRunning = True  #Booléen qui contrôle la boucle principale du jeu.


#Fonction d'affichage
def affiche(grille):
    print(grille[6] + " | " + grille[7] + " | " + grille[8])
    print("-" * 9)
    print(grille[3] + " | " + grille[4] + " | " + grille[5])
    print("-" * 9)
    print(grille[0] + " | " + grille[1] + " | " + grille[2])
   #affiche: Cette fonction imprime la grille de jeu sous forme de tableau 3x3, en utilisant des séparateurs pour une meilleure lisibilité.



def tour_du_joueur(grille):
    print("joueur → ",currentPlayer)
    choix_joueur = int(input("Choisi entre 1 et 9 :"))
    if 1 <= choix_joueur <= 9 and grille[choix_joueur - 1] == "-": #Vérifie que le choix est valide (entre 1 et 9) et 
        grille[choix_joueur - 1] = currentPlayer                   #que la case n'est pas déjà occupée. Sinon, elle rappelle la fonction pour demander un nouveau choix.
    else:
        print("valeur incorrecte ou emplacement déjà utilisé !")
        tour_du_joueur(grille)
        
        
def changement(currentPlayer):
    return "O" if currentPlayer=="X" else "X"        

def victoire(grille):
    global gameRunning #Utilise global gameRunning pour pouvoir modifier la variable de contrôle.
    if grille[6] == grille[7] == grille[8] == currentPlayer:
        print("le joueur",currentPlayer, "à gagné !")
        affiche(grille)
        gameRunning = False
    
    elif grille[3] == grille[4] == grille[5] == currentPlayer:
        print("le joueur",currentPlayer, "à gagné !")
        affiche(grille)
        gameRunning = False
    
    elif grille[0] == grille[1] == grille[2] == currentPlayer:
        print("le joueur",currentPlayer, "à gagné !")
        affiche(grille)
        gameRunning = False
        
    elif grille[6] == grille[3] == grille[0] == currentPlayer:
        print("le joueur",currentPlayer, "à gagné !")
        affiche(grille)
        gameRunning = False
    
    elif grille[7] == grille[4] == grille[1] == currentPlayer:
        print("le joueur",currentPlayer, "à gagné !")
        affiche(grille)
        gameRunning = False
    
    elif grille[8] == grille[5] == grille[2] == currentPlayer:
        print("le joueur",currentPlayer, "à gagné !")
        affiche(grille)
        gameRunning = False
    
    elif grille[0] == grille[4] == grille[8] == currentPlayer:
        print("le joueur",currentPlayer, "à gagné !")
        affiche(grille)
        gameRunning = False
    
    elif grille[6] == grille[4] == grille[2] == currentPlayer:
        print("le joueur",currentPlayer, "à gagné !")
        affiche(grille)
        gameRunning = False
    
    elif "-" not in grille:
        print("Match nul !")
        gameRunning = False
    
    else:
        print("Joueur",currentPlayer,)


       
       




while gameRunning:
    affiche(grille)
    tour_du_joueur(grille)
    victoire(grille)
    if gameRunning:
        currentPlayer = changement(currentPlayer)


       