# DEBUT
import random
scoreJoueur=0
scoreOrdinateur=0
def fonctionTour():
    if choixJoueur == 0:
        if choixOrdinateur == 0:
            return("égalité")
        elif choixOrdinateur == 1:
            return("perdu")
        elif choixOrdinateur == 2:
            return("gagnée")

    elif choixJoueur ==1:
        if choixOrdinateur == 0:
            return("gagnée")
        elif choixOrdinateur == 1:
            return("égalité")
        elif choixOrdinateur == 2:
            return("perdu")

    elif choixJoueur ==2:
        if choixOrdinateur == 0:
            return("perdu")
        elif choixOrdinateur == 1:
            return("gagnée")
        elif choixOrdinateur == 2:
            return("égalité")
    else:
        return("erreur")

while ((scoreJoueur<3) and (scoreOrdinateur< 3)):
    choixOrdinateur = random.randint(0,2)
    choixJoueur = int(input("pierre(0) , feuille (1) , ciseau (2)"))
    scoreTour = fonctionTour()
    
    if choixJoueur == 0:
        print("le joueur a fait pierre")
    elif choixJoueur == 1:
        print("le joueur a fait feuille")
    elif choixJoueur == 2:
        print("le joueur a fait ciseau")

    if choixOrdinateur == 0:
        print("l'ordinateur a fait pierre")
    elif choixOrdinateur == 1:
        print("l'ordinateur a fait feuille")
    elif choixOrdinateur == 2:
        print("l'ordinateur a fait ciseau")


    if (scoreTour == "gagnée" ):
        scoreJoueur  += 1
        print("Tour gagnant")
    elif (scoreTour == "perdu"):
        scoreOrdinateur  += 1
        print("Tour perdant")
    elif (scoreTour == "égalité"):
        print("Tour égalité")
    elif(scoreTour== "erreur"):
        print("erreur")
    
    print(scoreJoueur,scoreOrdinateur)

    if scoreJoueur == 3:
        print("bien joué , tu est fort")
    elif scoreOrdinateur == 3:
        print("tu est nul")
    #Fin